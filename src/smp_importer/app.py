import logging
import os
import pathlib

import fastapi
import fastapi.responses
import fastapi.staticfiles
import fastapi.templating
import httpx
import pydantic

from .logic import prepare_import_mapping


ROOT_DIR = pathlib.Path(__file__).parent
STATIC_DIR = ROOT_DIR / 'static'
TEMPLATES_DIR = ROOT_DIR / 'templates'
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
async def api_import_from_file(body_file: BodyFile):
    try:
        result = prepare_import_mapping(
            contents=body_file.contents,
            content_type=body_file.type,
        )
        return fastapi.responses.JSONResponse(content={
            'sourcce': 'file',
            'name': body_file.name,
            'actions': result['actions'],
        })
    except Exception as e:
        LOG.error(f'Error appeared: {str(e)}', exc_info=e)
        raise fastapi.HTTPException(status_code=500)


@app.post('/api/import-url', response_class=fastapi.responses.JSONResponse)
async def api_import_from_url(body_url: BodyURL):
    try:
        result = await fetch_from_url(body_url.url)
        return fastapi.responses.JSONResponse(content={
            'source': 'url',
            'url': body_url.url,
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
        return prepare_import_mapping(
            contents=r.content.decode(encoding=r.charset_encoding or 'utf-8'),
            content_type=r.headers.get('content-type'),
        )
