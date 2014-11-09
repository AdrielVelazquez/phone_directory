import os

ENVIRONMENT = "dev"
DEBUG = True

HOST = "127.0.0.1"
PORT = 5000
COUCHDB_SERVER = ""
PHONE_DB = "numbers-db"

# let custom config override defaults
if os.environ.get('PHONE_NUMBER_CONFIG', False):
    import imp
    imp.load_source('app.customconfig', os.environ['PHONE_NUMBER_CONFIG'])
    from app.customconfig import *
