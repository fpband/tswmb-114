# (c) @FarshidBand

from configs import Config
from core.database import Database

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
