import logging
import time
from fastapi import BackgroundTasks,APIRouter,HTTPException
from pydantic import BaseModel,Schema
from app.common.config import Config
from app.common.jira_models import WebHookModelIn, WebHookModelOut
from app.tasks.factory import Macro, event_factory

Config.init_config()
logger = logging.getLogger(__name__)
logger.info("jira events start")

router = APIRouter()

@router.post("/jira/events/{action}", tags=["jira","events"])
async def post_event(action:str, event:WebHookModelIn, background_tasks: BackgroundTasks):
   logger.info(f"POST event:[{action}]")
   
   ##add task to execute in background
   macro = Macro()
   macro.add(  event_factory(event.event.type, event) )
   
   #Return http response
   background_tasks.add_task( macro.run )
   return WebHookModelOut()