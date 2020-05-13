from typing import List
from pydantic import BaseModel,Schema
from enum import Enum, IntEnum

class WebHookModelIn(BaseModel):
    command: str
    
class WebHookModelOut(BaseModel):
   text: str = None