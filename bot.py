import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6186689074:AAE-QC_SF682gMoOcWbgH6OoOeNLOpPSzm0")

API_ID = int(os.environ.get("API_ID", "28185220"))

API_HASH = os.environ.get("API_HASH", "7775088403abbe110d5a38cfc75addce")

STRING = os.environ.get("STRING", "BQEwmScAIE-O8pyEewOvl4zu_aiYQ5IBdAOrj00s0Ls18gEdE3qQBFOEAZaHVkvwyXGeUPEX2g7wAcvrTjOcgXQrLoQ7x7WPLDWFM667M4ISDPOYerqGoChxFF8jRU2k7g6bWbFpUlCMNS3hHXx24txwjceLsF42-ixQNYVApWHanRgWMx-7NVVR-ab8FJ42UQWSa--PAmUw3m_ZIGyaZHmlX7hDUJeDi5BdCf9WHjbMTdFLUthdmc3o7jCVRUH2FMho30c_nmAP-JRYHNNOIf4MzLCQbwYJ5U5ouuzopTWYxuPuxinKtQ2_biaiei9TqLdl7wdQ0MYc_6iUY2Ej-SAICxw2EAAAAABpeCb7AA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
