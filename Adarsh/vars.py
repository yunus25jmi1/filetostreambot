# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = True
    API_ID = int(getenv('API_ID' , '7946647' , '7946647'))
    API_HASH = str(getenv('API_HASH' , '3d564ea96a493b54f8aa5ebb3408bb9f' , '3d564ea96a493b54f8aa5ebb3408bb9f'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '5986704794:AAE1FtyRn04GsPqji5P_HIwjbzzmUIExGkI' , '6115931607:AAEYFSE-ysN-rPZeUMEl-r2pymJAK4v8XPE'))
    name = str(getenv('name', 'yunusfilestreambot' , 'yunusfilestrembot-2.0'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60' , '60'))
    WORKERS = int(getenv('WORKERS', '4' , '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL' , '-1001917434512' , '-1001917434512'))
    PORT = int(getenv('PORT', 8080 , 8081))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0' , '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200" , "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5942676202" , "5942676202").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('Yunus25jmi'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'https://file.yunusplays.eu.org' )) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL' , 'mongodb+srv://yunus:yunus@cluster0.kuyaznm.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
