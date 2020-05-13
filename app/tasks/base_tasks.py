import logging
import os
import json
from pydantic import BaseModel
from app.common.jira_models import WebHookModelIn,WebHookModelOut
import app.common.util
from app.common.config import Config
from abc import ABC,abstractmethod


Config.init_config()
logger = logging.getLogger(__name__)
logger.info("tasks start")

class Task(ABC):
    
    def __init__(self,event:BaseModel):
        self.event_in=event
        self.logger = logger
        #self.CHANNEL_TGX_ANNOUNCEMENTS = Config.get_or_else('SLACK', 'CHANNEL_TGX_ANNOUNCEMENTS',None)
        #self.CHANNEL_ALL_ANNOUNCEMENTS = Config.get_or_else('SLACK', 'CHANNEL_ALL_ANNOUNCEMENTS',None)
        #self.web_client = slack.WebClient(token=Config.get_or_else('SLACK', 'BOT_TOKEN',None), run_async=True)
      
    @abstractmethod
    async def execute(self): pass
   
class Command(Task):
    @abstractmethod
    async def execute(self): pass
    
    
class Event(Task):pass