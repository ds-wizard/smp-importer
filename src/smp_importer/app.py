import logging
import os
import pathlib

import fastapi
import fastapi.responses
import fastapi.staticfiles
import fastapi.templating


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


@app.get('/api/import', response_class=fastapi.responses.JSONResponse)
async def list_fips(request: fastapi.Request):
    try:
        return fastapi.responses.JSONResponse(content={'text': 'Hello'})
    except Exception as e:
        LOG.error(f'Error appeared: {str(e)}', exc_info=e)
        raise fastapi.HTTPException(status_code=500)
