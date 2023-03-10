import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '29158577'))
API_HASH = environ.get('API_HASH', '5a31bb001fafce5f0c8669b0a8138280')
BOT_TOKEN = environ.get('BOT_TOKEN', '5822315641:AAFqkhrkwEsj4if8BE0nrzbLBECcObntvjw')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
# Bot images & videos
PICS = (environ.get('PICS', 'https://te.legra.ph/file/f6650a4eb987ab0900afb.jpg https://te.legra.ph/file/d321601bcbdb21962276b.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/e37213acf66d814cf0bcf.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/2a888a370f479f4338f7c.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5134179712').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001736259211').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5134179712').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001827834176')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", "<b>???? ????????????????????????'???? ???????????????? ???????????????????????????????? ???????????????????????????? ???????? ????????????????</b>\n\n??? <b><i>If You Want Your Request, Then Buy Our Premium ??? @ORGPrime</i></b>"))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://orgprime:orgprime@cluster0.t89i6ib.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Collection')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001784051585))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'uhdimax')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '<b>[ @ORGPrime ]</b> - <code>{file_name}</code> <b>\n\n?????? Size = {file_size}</b> \n\n<b><i> ?? ?????????????????????????? ??</i> [@UHDiMAX](https://t.me/uhdimax)</b>')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '<b>[ @ORGPrime ]</b> - <code>{file_name}</code> <b>\n\n?????? Size = {file_size}</b> \n\n<b><i> ?? ?????????????????????????? ??</i> [@UHDiMAX](https://t.me/uhdimax)</b>')
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", '???? ????????????????????: <a href={url}>{title}</a> \n???? ????????????????: {year} \n?????? ????????????????????????????: {rating}/ 10  \n???? ????????????????????????: {genres} \n\n???? ???????????????????????????? ???????? [???@UHDiMAX???](t.me/uhdimax)')
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001736259211')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
