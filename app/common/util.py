import logging
import json
from pydantic import BaseModel
from string import Template
from typing import (List)
from app.common.config import Config

Config.init_config()
logger = logging.getLogger(__name__)
logger.info("util start")