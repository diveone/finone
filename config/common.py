"""
CONFIGURATION
=============
****************************************************************
     SENSITIVE CREDENTIALS ARE **NEVER** TO BE STORED HERE.
****************************************************************

Basic settings common to all applications live here. For local:
* Open config/dev.py
* Modify or add any settings
* Add env variable: APP_CONFIG_FILE=/path/to/config/dev.py
"""
import logging, os

DEBUG = False

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = 'finone.log'
LOGGING_LEVEL = logging.DEBUG

DB_NAME = os.environ['DB_FINONE']
DB_USER = os.environ['DB_USER']
DB_PWD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True

MORTECH_LICENSEKEY = os.getenv('MORTECH_LICENSEKEY')
MORTECH_THIRDPARTY_NAME = os.getenv('MORTECH_THIRDPARTY_NAME')
MORTECH_CUSTOMER_ID = os.getenv('MORTECH_CUSTOMER_ID')
MORTECH_EMAIL = os.getenv('MORTECH_EMAIL')
MORTECH_ENDPOINT = os.getenv('MORTECH_ENDPOINT')

# app.config not reading dev.py XXXme
LOCAL_ENDPOINT = "http://localhost:3333/test"
