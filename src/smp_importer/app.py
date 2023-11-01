import base64
import logging
import mimetypes
import os
import pathlib

import fastapi
import fastapi.responses
import fastapi.staticfiles
import fastapi.templating
import httpx
import pydantic

from .importer import process


ROOT_DIR = pathlib.Path(__file__).parent
STATIC_DIR = ROOT_DIR / 'static'
TEMPLATES_DIR = ROOT_DIR / 'templates'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
LOG = logging.getLogger(__name__)


app = fastapi.FastAPI()
app.mount(
    path='/static',
    app=fastapi.staticfiles.StaticFiles(directory=STATIC_DIR),
    name='static',
)
templates = fastapi.templating.Jinja2Templates(directory=TEMPLATES_DIR)


class BodyURL(pydantic.BaseModel):
    url: str


class BodyFile(pydantic.BaseModel):
    name: str
    contents: str
    type: str
    bytesize: int


class BodyGitHubPublic(pydantic.BaseModel):
    owner: str
    repo: str
    file: str


@app.get('/', response_class=fastapi.responses.HTMLResponse)
async def get_index(request: fastapi.Request):
    return templates.TemplateResponse(
        name='index.html.j2',
        context={
            'request': request,
            'debug': os.environ.get('IMPORTER_DEBUG', '') == 'true',
            'development': os.environ.get('IMPORTER_DEV', '') == 'true',
        },
    )


@app.post('/api/import-file', response_class=fastapi.responses.JSONResponse)
async def api_import_from_file(body: BodyFile):
    try:
        result = process(
            content=body.contents,
            content_type=body.type,
        )
        return fastapi.responses.JSONResponse(content={
            'sourcce': 'file',
            'name': body.name,
            'actions': result['actions'],
        })
    except Exception as e:
        LOG.error(f'Error appeared: {str(e)}', exc_info=e)
        raise fastapi.HTTPException(status_code=500)


@app.post('/api/import-url', response_class=fastapi.responses.JSONResponse)
async def api_import_from_url(body: BodyURL):
    try:
        result = await fetch_from_url(body.url)
        return fastapi.responses.JSONResponse(content={
            'source': 'url',
            'url': body.url,
            'actions': result['actions'],
        })
    except Exception as e:
        LOG.error(f'Error appeared: {str(e)}', exc_info=e)
        raise fastapi.HTTPException(status_code=500)


@app.post('/api/import-github-public', response_class=fastapi.responses.JSONResponse)
async def api_import_from_github_public(body: BodyGitHubPublic):
    try:
        result = await fetch_from_github_public(body.owner, body.repo, body.file)
        return fastapi.responses.JSONResponse(content={
            'source': 'github',
            'owner': body.owner,
            'repo': body.repo,
            'file': body.file,
            'actions': result['actions'],
        })
    except Exception as e:
        LOG.error(f'Error appeared: {str(e)}', exc_info=e)
        raise fastapi.HTTPException(status_code=500)


# ----- logic

async def fetch_from_url(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        r.raise_for_status()
        return process(
            content=r.content.decode(encoding=r.charset_encoding or 'utf-8'),
            content_type=r.headers.get('content-type'),
        )


async def fetch_from_github_public(owner: str, repo: str, file: str) -> dict:
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    if GITHUB_TOKEN is not None:
        headers['Authorization'] = f'Bearer {GITHUB_TOKEN}'

    async with httpx.AsyncClient() as client:
        r = await client.get(
            url=f'https://api.github.com/repos/{owner}/{repo}/contents/{file}',
            headers=headers
        )
        r.raise_for_status()

        data = r.json()
        if data.get('encoding') == 'base64':
            return process(
                content=base64.b64decode(data['content']).decode('utf-8'),
                content_type=mimetypes.guess_type(data['url'])[0] or 'text/plain',
            )
        raise RuntimeError('Unexpected response from GitHub')
