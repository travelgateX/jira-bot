import json
import logging
import hashlib
import hmac
import json
from time import time

from fastapi import Security, Depends, FastAPI, Header, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey

from starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette_exporter import PrometheusMiddleware, handle_metrics

from app.routers import (jira_events)
from app.common.config import Config


Config.init_config()
logger = logging.getLogger(__name__)
logger.info("main start")

API_KEY = Config.get_or_else('APP', 'API_KEY_NAME',None)
API_KEY_NAME = Config.get_or_else('APP', 'API_KEY_NAME',None)
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header)
):
    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


async def log_request(request: Request):
   for header in request.headers:
      logger.info(f"Request header:[{header}]:[{request.headers[header]}]")   
   body = await request.body()
   data_str = body.decode()
   logger.info(f"Request body:[{data_str}]")
 


app = FastAPI()

#starlette metrics
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

app.include_router(
   jira_events.router,
   tags=["jira","events"],
   dependencies=[Depends(get_api_key)]
)

