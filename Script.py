class script(object):
    START_TXT = """ğ¸ğ...ğ¸ğ... {} ğ

<b><u>ğ¨'ğ ğ¯ğğğ¾ğğ¿ğğ @UHDiMAX ğ ğğğ-ğ¥ğğğğ¾ğ ğ¡ğğ ğ¸ğğ ğ¢ğºğ ğ´ğğ¾ ğ¬ğ¾ ğ ğ ğ  ğ ğğğ-ğ¿ğğğğ¾ğ ğğ ğ¸ğğğ ğ¦ğğğğ.</u></b>

Its Easy To Use Me:-
Just Add Me To Your Group As Admin, 
Thats All, i will Provide Movies There...ğ¤

â ï¸ ğ¬ğğğ¾ ğ§ğ¾ğğ ğ§ğğ /help

<b>ğ ğ¯ğğğ¾ğğ¾ğ½ ğ»ğ @UHDiMAX</b>"""

    HELP_TXT = """ğğ»ââï¸   ğ§ğ¾ğğğğğ  {} ğ¤

â Iğ'ğ ğ­ğğğ¾ ğ¢ğğğğğğ¼ğºğğ¾ğ½...ğ¤

Just Add Me To Your Group As Admin, 
Thats All, i will Provide Movies There...ğ¤

â ğ ğğºğğğºğ»ğğ¾ ğ¢ğğğğºğğ½ğ
     
 /alive - Check I'm Alive..
 /status - Bot Status
 /info - User info
 /ping - To get your ping
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (ğ®ğğğ¾ğ ğ®ğğğ)

â <u>ğ­ğğğğ¼ğ¾</u> ğ:-

ğ£ğğğ ğ²ğğºğ ğ¬ğ¾...ğ¤

ğ ğ¯ğğğ¾ğğ¾ğ½ ğ»ğ @UHDiMAX"""

    ABOUT_TXT = """<b>â About:</b>
â ğ¢ğğ¾ğºğğğ : <a href='https://t.me/uhdsupport'>ğ³ğğğ ğ¯ğ¾ğğğğ</a>
â ğ«ğºğğğğºğğ¾ : ğ¯ğğğğğ ğ¥.0
â ğ«ğğ»ğğºğğ : ğ¯ğğğğğğºğ ğºğğğğ¼ğğ ğ¢.ğ£ğ©.ğ£ 
â ğ£ğºğğºğ»ğºğğ¾ : <a href='https://www.mongodb.com'>ğ¬ğğğğğ£ğ¡ ğ¥ğğ¾ğ¾ ğ³ğğ¾ğ</a>
â ğ¡ğğğğ½ ğ²ğğºğğğ : v1.0.1 [BeTa]
â ğ²ğğğğğğ ğ¦ğğğğ : <a href='https://t.me/uhdimaxmovies'>Join Group</a>
"""

    SOURCE_TXT = """<b>NOTE:</b>
Special Thanks to â¡ @UHDiMAX â¡

<b>DEVS:</b>
- <a href=https://t.me/uhdsupport>UHDSupport</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>
    
- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message.

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Bot supports buttons with any telegram media type.
2. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/uhdimax)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Há´Êá´: <b>á´á´á´á´ ê°ÉªÊá´á´Ê</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.

<b>Ná´á´á´: Aá´á´á´FÉªÊá´á´Ê</b>
1. Aá´á´ á´Êá´ Êá´á´ á´s á´á´á´ÉªÉ´ á´É´ Êá´á´Ê É¢Êá´á´á´.
2. Usá´ /connect á´É´á´ á´á´É´É´á´á´á´ Êá´á´Ê É¢Êá´á´á´ á´á´ á´Êá´ Êá´á´.
3. Usá´ /settings á´É´ Êá´á´'s PM á´É´á´ á´á´ÊÉ´ á´É´ Aá´á´á´FÉªÊá´á´Ê á´É´ á´Êá´ sá´á´á´ÉªÉ´É¢s á´á´É´á´."""

    CONNECTION_TXT = """Há´Êá´: <b>á´á´É´É´á´á´á´Éªá´É´ê±</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Há´Êá´: Exá´Êá´ Má´á´á´Êá´s
<b>Ná´á´á´:</b>
These are the extra features of Bot.

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>É´á´á´á´:</b>
TÊÉªs Má´á´á´Êá´ OÉ´ÊÊ Wá´Êá´s Fá´Ê MÊ Aá´á´ÉªÉ´s.

<b>Commands and Usage:</b>
â¢ /logs - <code>á´á´ É¢á´á´ á´Êá´ Êá´á´á´É´á´ á´ÊÊá´Êê±</code>
â¢ /stats - <code>á´á´ É¢á´á´ ê±á´á´á´á´ê± á´ê° ê°ÉªÊá´ê± ÉªÉ´ á´Ê. [TÊÉªs Cá´á´á´á´É´á´ Cá´É´ Bá´ Usá´á´ BÊ AÉ´Êá´É´á´]</code>
â¢ /delete - <code>á´á´ á´á´Êá´á´á´ á´ ê±á´á´á´Éªê°Éªá´ ê°ÉªÊá´ ê°Êá´á´ á´Ê.</code>
â¢ /users - <code>á´á´ É¢á´á´ ÊÉªê±á´ á´ê° á´Ê á´ê±á´Êê± á´É´á´ Éªá´ê±.</code>
â¢ /chats - <code>á´á´ É¢á´á´ ÊÉªê±á´ á´ê° á´Ê á´Êá´á´ê± á´É´á´ Éªá´ê±</code>
â¢ /leave  - <code>á´á´ Êá´á´á´ á´ ê°Êá´á´ á´ á´Êá´á´.</code>
â¢ /disable  -  <code>á´á´ á´Éªê±á´ÊÊá´ á´ á´Êá´á´.</code>
â¢ /ban  - <code>á´á´ Êá´É´ á´ á´ê±á´Ê.</code>
â¢ /unban  - <code>á´á´ á´É´Êá´É´ á´ á´ê±á´Ê.</code>
â¢ /channel - <code>á´á´ É¢á´á´ ÊÉªê±á´ á´ê° á´á´á´á´Ê á´á´É´É´á´á´á´á´á´ á´Êá´É´É´á´Êê±</code>
â¢ /broadcast - <code>á´á´ ÊÊá´á´á´á´á´ê±á´ á´ á´á´ê±ê±á´É¢á´ á´á´ á´ÊÊ á´ê±á´Êê±</code>
â¢ /group_broadcast - <code>Tá´ ÊÊá´á´á´á´á´sá´ á´ á´á´ssá´É¢á´ á´á´ á´ÊÊ á´á´É´É´á´á´á´á´á´ É¢Êá´á´á´s.</code>
â¢ /gfilter - <code>á´á´ á´á´á´ É¢Êá´Êá´Ê ÒÉªÊá´á´Ês</code>
â¢ /gfilters - <code>á´á´ á´ Éªá´á´¡ ÊÉªsá´ á´Ò á´ÊÊ É¢Êá´Êá´Ê ÒÉªÊá´á´Ês</code>
â¢ /delg - <code>á´á´ á´á´Êá´á´á´ á´ sá´á´á´ÉªÒÉªá´ É¢Êá´Êá´Ê ÒÉªÊá´á´Ê</code>
â¢ /request - <code>Tá´ sá´É´á´ á´ Má´á´ Éªá´/Sá´ÊÉªá´s Êá´á´Ì¨á´á´sá´ á´á´ Êá´á´ á´á´á´ÉªÉ´s. OÉ´ÊÊ á´¡á´Êá´s á´É´ sá´á´á´á´Êá´ É¢Êá´á´á´. [TÊÉªs Cá´á´á´á´É´á´ Cá´É´ Bá´ Usá´á´ BÊ AÉ´Êá´É´á´]</code>
â¢ /delallg - <code>Tá´ á´á´Êá´á´á´ á´ÊÊ GÒÉªÊá´á´Ês ÒÊá´á´ á´Êá´ Êá´á´'s á´á´á´á´Êá´sá´.</code>
â¢ /deletefiles - <code>Tá´ á´á´Êá´á´á´ Cá´á´RÉªá´ á´É´á´ PÊá´DVD FÉªÊá´s ÒÊá´á´ á´Êá´ Êá´á´'s á´á´á´á´Êá´sá´.</code>"""

    STATUS_TXT = """â ğğ¾ğğ°ğ» ğµğ¸ğ»ğ´ğ: <code>{}</code>
â ğğ¾ğğ°ğ» ğğğ´ğğ: <code>{}</code>
â ğğ¾ğğ°ğ» ğ²ğ·ğ°ğğ: <code>{}</code>
â ğğğ´ğ³ ğğğ¾ğğ°ğ¶ğ´: <code>{}</code> 
â ğµğğ´ğ´ ğğğ¾ğğ°ğ¶ğ´: <code>{}</code> """

    LOG_TEXT_G = """#NewGroup
GÊá´á´á´ = {}(<code>{}</code>)
Total Members = <code>{}</code>
Aá´á´á´á´ BÊ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Ná´á´á´ - {}"""

    ALRT_TXT = """Hello {},
This is Not your Request.
Request Yourself..."""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CUDNT_FND = """<b><i>
ğ¨ ğ¼ğğğğ½ğ'ğ ğ¿ğğğ½ ğºğğğğğğğ ğğ¾ğğºğğ¾ğ½ ğğ ğğğºğ. ğ£ğğ½ ğğğ ğğ¾ğºğ ğºğğ ğğğ¾ ğğ¿ ğğğ¾ğğ¾?</i></b>"""

    I_CUDNT = """<b>ğ¨ ğ¼ğğğğ½ğ'ğ ğ¿ğğğ½ ğºğğğğğğğ ğğ¾ğğºğğ¾ğ½ ğğ ğğğºğ</b>\n\nâ¼ <b><i>If You Want Your Request Then Buy Our Premium â¶ @ORGPrime</i></b>"""

    I_CUD_NT = """<b>ğ¨ ğ¼ğğğğ½ğ'ğ ğ¿ğğğ½ ğºğğğğğğğ ğğ¾ğğºğğ¾ğ½ ğğ ğğğºğ</b>\n\nâ¼ <b><i>If You Want Your Request Then Buy Our Premium â¶ @ORGPrime</i></b>"""

    MVE_NT_FND = """<b>ğ¨ ğ¼ğğğğ½ğ'ğ ğ¿ğğğ½ ğºğğğğğğğ ğğ¾ğğºğğ¾ğ½ ğğ ğğğºğ</b>\n\nâ¼ <b><i>If You Want Your Request Then Buy Our Premium â¶ @ORGPrime</i></b>"""

    TOP_ALRT_MSG = """ğ¢ğğ¾ğ¼ğğğğ ğ¿ğğ ğğğ¾ğğ ğğ ğ£ğºğğºğ»ğºğğ¾..."""

    MELCOW_ENG = """<b>Hey {}, Welcome to {}</b> 

â¢ ğ­ğ ğ¯ğğğğ, ğ­ğ ğ¯ğğğ, ğ­ğ ğ®ğğğ¾ğ ğ ğ»ğğğ¾ğ
â¢ ğ ğğ ğ¸ğğğ ğ¬ğğğğ¾ğ ğ¶ğğğ ğ¢ğğğğ¾ğ¼ğ ğ²ğğ¾ğğğğğ
â¢ ğ²ğğºğğğ¾ğğ ğ²ğğºğ ğ ğğºğ
â¢ ğ¥ğ¾ğ¾ğ ğ¥ğğ¾ğ¾ ğ³ğ ğ±ğ¾ğğğğ ğ ğğ ğ¤ğğğğğ ğ³ğ ğ ğ½ğğğğ ğğğğğ @admin

<u>ğ¥ğ²ğ¾ğğ²ğğğ ğğ¼ğ¿ğºğ®ğğ</u>

â¢ Avatar 2009
â¢ ğ£ğºğğ S01
â¢ ğ¥ğğğ¾ğğ½ğ S03 1080ğ

â¼ï¸ğğ¼ğ»ğ ğ®ğ±ğ± ğğ¼ğ¿ğ±ğ & ğğğºğ¯ğ¼ğ¹ğ ğ¹ğ¶ğ¸ğ² , . -  send, link, movie, series ğ²ğğ°â¼ï¸"""

    OWNER_INFO = """<b> OWNER :-</b>

â ğ¢ğğ¾ğºğğğ : <a href='https://t.me/uhdsupport'>ğ³ğğğ ğ¯ğ¾ğğğğ</a>

â ğ²ğğğğğğ ğ¦ğğğğ : <a href='https://t.me/uhdimaxmovies'>ğ³ğºğ ğ§ğ¾ğğ¾</a>
"""

    NORSLTS = """
#NoResults 

ID <b>: {}</b>

Name <b>: {}</b>

Message <b>: {}</b>"""

    CAPTION = """
ğ [ @ORGPrime ] - <code{file_name}</code>

ğ <em>Size</em>: <code>{file_size}</code> 

â¤ï¸â<i> â¤ÍÍğâ¡ğ¼ğ¶ğ» Â»</i> [@UHDiMAX](https://t.me/uhdimax) """

    IMDB_TEMPLATE_TXT = """
ğ· ğ³ğğğğ¾: <a href={url}>{title}</a> 
ğ® ğ¸ğ¾ğºğ: {year} \nâ­ï¸ ğ±ğºğğğğğ: {rating}/ 10  
ğ­ ğ¦ğ¾ğğ¾ğğ: {genres} 

ğ <i>ğ¯ğğğ¾ğğ¾ğ½ ğ¡ğ</i>[ã@UHDiMAXã](t.me/uhdimax)"""
    
    ALL_FILTERS = """
<b>Hey {}, These are My Three Types of Filters.</b>"""
    
    GFILTER_TXT = """
<b>Wá´Êá´á´á´á´ á´á´ GÊá´Êá´Ê FÉªÊá´á´Ês. GÊá´Êá´Ê FÉªÊá´á´Ês á´Êá´ á´Êá´ ÒÉªÊá´á´Ês sá´á´ ÊÊ Êá´á´ á´á´á´ÉªÉ´s á´¡ÊÉªá´Ê á´¡ÉªÊÊ á´¡á´Êá´ á´É´ á´ÊÊ É¢Êá´á´á´s.</b>

Aá´ á´ÉªÊá´ÊÊá´ Cá´á´á´á´É´á´s:
â¢ /gfilter - <code>Tá´ á´Êá´á´á´á´ á´ É¢Êá´Êá´Ê ÒÉªÊá´á´Ê.</code>
â¢ /gfilters - <code>Tá´ á´ Éªá´á´¡ á´ÊÊ É¢Êá´Êá´Ê ÒÉªÊá´á´Ês.</code>
â¢ /delg - <code>Tá´ á´á´Êá´á´á´ á´ á´á´Êá´Éªá´á´Êá´Ê É¢Êá´Êá´Ê ÒÉªÊá´á´Ê.</code>
â¢ /delallg - <code>á´á´ á´á´Êá´á´á´ á´ÊÊ É¢Êá´Êá´Ê ê°ÉªÊá´á´Êê±.</code>"""
    
    FILE_STORE_TXT = """
<b>FÉªÊá´ sá´á´Êá´ Éªs á´Êá´ Òá´á´á´á´Êá´ á´¡ÊÉªá´Ê á´¡ÉªÊÊ á´Êá´á´á´á´ á´ sÊá´Êá´á´ÊÊá´ ÊÉªÉ´á´ á´Ò á´ sÉªÉ´É¢Êá´ á´Ê á´á´Êá´Éªá´Êá´ ÒÉªÊá´s.</b>

Aá´ á´ÉªÊá´ÊÊá´ á´á´á´á´á´É´á´s:
â¢ /batch - <code>Tá´ á´Êá´á´á´á´ á´ Êá´á´á´Ê ÊÉªÉ´á´ á´Ò á´á´Êá´Éªá´Êá´ ÒÉªÊá´s.</code>
â¢ /link - <code>Tá´ á´Êá´á´á´á´ á´ sÉªÉ´É¢Êá´ ÒÉªÊá´ sá´á´Êá´ ÊÉªÉ´á´.</code>
â¢ /pbatch - <code>Já´sá´ ÊÉªá´á´ /batch, Êá´á´ á´Êá´ ÒÉªÊá´s á´¡ÉªÊÊ Êá´ sá´É´á´ á´¡Éªá´Ê Òá´Êá´¡á´Êá´ Êá´sá´ÊÉªá´á´Éªá´É´s.</code>
â¢ /plink - <code>Já´sá´ ÊÉªá´á´ /link, Êá´á´ á´Êá´ ÒÉªÊá´ á´¡ÉªÊÊ Êá´ sá´É´á´ á´¡Éªá´Ê Òá´Êá´¡á´Êá´ Êá´sá´ÊÉªá´á´Éªá´É´.</code>"""

    RESTART_TXT = """
<b>Bá´á´ Rá´sá´á´Êá´á´á´ !

ğ Dá´á´á´ : <code>{}</code>
â° TÉªá´á´ : <code>{}</code>
ğ TÉªá´á´á´¢á´É´á´ : <code>Asia/Kolkata</code>
ğ ï¸ Bá´ÉªÊá´ Sá´á´á´á´s: <code>v2.7.1 [ Sá´á´ÊÊá´ ]</code></b>"""

    LOGO = """
â¡ @UHDiMAX â¡"""
