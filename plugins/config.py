import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7595256869:AAEdBHPlyGhoRmydfFH5j1wEZ_Et9dKKvfE")
    
    API_ID = int(os.environ.get("API_ID", "29148812"))
    
    API_HASH = os.environ.get("API_HASH", "d8aac7789e949db80b09c1a37b21cbce")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = "1AZWarzUBuyRKruqSGqJAzkUSfmRseZm9WK3vfkHHL9DVuuitAEAeXrf-z-zcBdVQ6GCNOyaHiREd9TByi9wMwHK4LLuC6v5ehI9Q_TAv1gi0R7h37i5BNcG_IrfR-OrG-ZXeD5zG0He7CfmD_MN0-iGbJNfndeBLdr3Tv90KpNDphf0DpjysTltoROvVAaw8gDrn6H0-TsydnyyX_FhU8jEkOW04nn97DVdz0TetdonVXxTYkYDtEIRuKkx0Q-fvTuIWSn7Yjd1f_g1Xnr6haWQcTU7YIMpL_pTJgdnfLGK6s4tFDTcaNMkIYESaEB-yjnUkPpnsw54BvJq1qcCYfq7tY1ib2oU="
    
    FREE_USER_MAX_FILE_SIZE = 2097152000

    MAX_SPLIT_SIZE = 4187407334
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    DEF_WATER_MARK_FILE = "NightMovieBackUpBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://alinomali1:lMk1MXjp34Ndwwrt@cluster0.lal5y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "NightMovieBackUpBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002293983513"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002293983513")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5581322718"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Nmupload_bot")
                                  
