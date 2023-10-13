import logging
import os
from datetime import datetime, timedelta
import pandas as pd

# Disable all logging output to the console
logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger("cmdstanpy").setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("prophet")
logger.setLevel(logging.ERROR)
logger_cmdstanpy = logging.getLogger("cmdstanpy")
logger_cmdstanpy.setLevel(logging.ERROR)
logging.getLogger("cmdstanpy").setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


