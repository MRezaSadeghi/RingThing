from pathlib import Path

ROOT = Path(__file__).parent.parent


# logger files
LOGRECORDER_FOLDER = ROOT / "logrecorder"
LOG_DATA_FOLDER = LOGRECORDER_FOLDER / "log_data"
LOGGER_CONFIG = LOGRECORDER_FOLDER / "logger.ini"
LOG_FILE = LOG_DATA_FOLDER / "log.txt"
