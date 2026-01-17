# import logging
# import os
# from datetime import datetime

# # project root = one level above src
# PROJECT_ROOT = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..")
# )

# LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
# os.makedirs(LOGS_DIR, exist_ok=True)

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
#     force=True
# )

# logger = logging.getLogger()



# # import logging
# # import os
# # from datetime import datetime

# # LOG_DIR = os.path.join(os.getcwd(), "logs")
# # os.makedirs(LOG_DIR, exist_ok=True)

# # LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# # LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# # logging.basicConfig(
# #     filename=LOG_FILE_PATH,
# #     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
# #     level=logging.INFO,
# # )

# # # logger = logging.getLogger()

import logging
import os
from datetime import datetime
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)  # 🔥 PRINTS TO CONSOLE
    ],
)
# logger = logging.getLogger()
logging.info("LOGGER INITIALIZED SUCCESSFULLY")
