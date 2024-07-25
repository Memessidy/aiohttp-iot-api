import os
from dotenv import load_dotenv, find_dotenv
import logging

load_dotenv('.env.local')

# logging
logger = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Postgresql
database_name = os.getenv('DATABASE_NAME')
username = os.getenv('DATABASE_USERNAME')
password = os.getenv('DATABASE_PASSWORD')
host = os.getenv('HOST')

