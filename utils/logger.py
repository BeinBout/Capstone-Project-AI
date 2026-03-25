import sys
from loguru import logger
from core.config import settings

service_mode = settings.SERVICE_MODE
log_level = "DEBUG" if service_mode == "development" else "WARNING"

logger.remove()
logger.add(sys.stderr, level=log_level)