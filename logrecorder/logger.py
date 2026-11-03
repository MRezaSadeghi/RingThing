import logging
import logging.config

from config import paths

logging.config.fileConfig(
    paths.LOGGER_CONFIG,
    defaults={"LOG_FILE": str(paths.LOG_FILE).replace("\\", "/")},
    disable_existing_loggers=False,
)

logger = logging.getLogger(__name__)
