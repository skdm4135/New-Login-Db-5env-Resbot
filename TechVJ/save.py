# # Don't Remove Credit Tg - @VJ_Botz
# # Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# # Ask Doubt on telegram @KingVJ01

# import asyncio 
# import pyrogram
# from pyrogram import Client, filters
# from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 
# import time
# import os
# import threading
# import json
# from config import API_ID, API_HASH
# from database.db import database 
# from TechVJ.strings import strings, HELP_TXT

# def get(obj, key, default=None):
#     try:
#         return obj[key]
#     except:
#         return default


# async def downstatus(client: Client, statusfile, message):
#     while True:
#         if os.path.exists(statusfile):
#             break

#         await asyncio.sleep(3)
      
#     while os.path.exists(statusfile):
#         with open(statusfile, "r") as downread:
#             txt = downread.read()
#         try:
#             await client.edit_message_text(message.chat.id, message.id, f"Downloaded : {txt}")
#             await asyncio.sleep(10)
#         except:
#             await asyncio.sleep(5)


# # upload status
# async def upstatus(client: Client, statusfile, message):
#     while True:
#         if os.path.exists(statusfile):
#             break

#         await asyncio.sleep(3)      
#     while os.path.exists(statusfile):
#         with open(statusfile, "r") as upread:
#             txt = upread.read()
#         try:
#             await client.edit_message_text(message.chat.id, message.id, f"Uploaded : {txt}")
#             await asyncio.sleep(10)
#         except:
#             await asyncio.sleep(5)


# # progress writer
# def progress(current, total, message, type):
#     with open(f'{message.id}{type}status.txt', "w") as fileup:
#         fileup.write(f"{current * 100 / total:.1f}%")


# # start command
# @Client.on_message(filters.command(["start"]))
# async def send_start(client: Client, message: Message):
#     buttons = [[
#         InlineKeyboardButton("𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭", url = "https://t.me/Farooq_is_King")
#     ],[
#         InlineKeyboardButton('🔍 WD Topic Group', url='https://t.me/Op_Topic_Group'),
#         InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Opleech_WD')
# 	]]
#     reply_markup = InlineKeyboardMarkup(buttons)
#     await client.send_message(message.chat.id, f"<b>👋 Hi {message.from_user.mention}, I am Save Restricted Content Bot, I can send you restricted content by its post link.\n\nFor downloading restricted content /login first.\n\nKnow how to use bot by - /help</b>", reply_markup=reply_markup, reply_to_message_id=message.id)
#     return


# # help command
# @Client.on_message(filters.command(["help"]))
# async def send_help(client: Client, message: Message):
#     await client.send_message(message.chat.id, f"{HELP_TXT}")

# @Client.on_message(filters.text & filters.private)
# async def save(client: Client, message: Message):
#     if "https://t.me/" in message.text:
#         datas = message.text.split("/")
#         temp = datas[-1].replace("?single","").split("-")
#         fromID = int(temp[0].strip())
#         try:
#             toID = int(temp[1].strip())
#         except:
#             toID = fromID
#         for msgid in range(fromID, toID+1):
#             # private
#             if "https://t.me/c/" in message.text:
#                 user_data = database.find_one({'chat_id': message.chat.id})
#                 if not get(user_data, 'logged_in', False) or user_data['session'] is None:
#                     await client.send_message(message.chat.id, strings['need_login'])
#                     return
#                 acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
#                 await acc.connect()
#                 chatid = int("-100" + datas[4])
#                 await handle_private(client, acc, message, chatid, msgid)
    
#             # bot
#             elif "https://t.me/b/" in message.text:
#                 user_data = database.find_one({"chat_id": message.chat.id})
#                 if not get(user_data, 'logged_in', False) or user_data['session'] is None:
#                     await client.send_message(message.chat.id, strings['need_login'])
#                     return
#                 acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
#                 await acc.connect()
#                 username = datas[4]
#                 try:
#                     await handle_private(client, acc, message, username, msgid)
#                 except Exception as e:
#                     await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            
# 	        # public
#             else:
#                 username = datas[3]

#                 try:
#                     msg = await client.get_messages(username, msgid)
#                 except UsernameNotOccupied: 
#                     await client.send_message(message.chat.id, "The username is not occupied by anyone", reply_to_message_id=message.id)
#                     return
#                 try:
#                     await client.copy_message(message.chat.id, msg.chat.id, msg.id, reply_to_message_id=message.id)
#                 except:
#                     try:    
#                         user_data = database.find_one({"chat_id": message.chat.id})
#                         if not get(user_data, 'logged_in', False) or user_data['session'] is None:
#                             await client.send_message(message.chat.id, strings['need_login'])
#                             return
#                         acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
#                         await acc.connect()
#                         await handle_private(client, acc, message, username, msgid)
                        
#                     except Exception as e:
#                         await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

#             # wait time
#             await asyncio.sleep(3)


# # handle private
# async def handle_private(client: Client, acc, message: Message, chatid: int, msgid: int):
#     msg: Message = await acc.get_messages(chatid, msgid)
#     msg_type = get_message_type(msg)
#     chat = message.chat.id
#     if "Text" == msg_type:
#         try:
#             await client.send_message(chat, msg.text, entities=msg.entities, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
#             return

#     smsg = await client.send_message(message.chat.id, 'Downloading', reply_to_message_id=message.id)
#     dosta = asyncio.create_task(downstatus(client, f'{message.id}downstatus.txt', smsg))
#     try:
#         file = await acc.download_media(msg, progress=progress, progress_args=[message,"down"])
#         os.remove(f'{message.id}downstatus.txt')
        
#     except Exception as e:
#         await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)  
    
#     upsta = asyncio.create_task(upstatus(client, f'{message.id}upstatus.txt', smsg))

#     if msg.caption:
#         caption = msg.caption
#     else:
#         caption = None
            
#     if "Document" == msg_type:
#         try:
#             ph_path = await acc.download_media(msg.document.thumbs[0].file_id)
#         except:
#             ph_path = None
        
#         try:
#             await client.send_document(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
#         if ph_path != None: os.remove(ph_path)
        

#     elif "Video" == msg_type:
#         try:
#             ph_path = await acc.download_media(msg.video.thumbs[0].file_id)
#         except:
#             ph_path = None
        
#         try:
#             await client.send_video(chat, file, duration=msg.video.duration, width=msg.video.width, height=msg.video.height, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
#         if ph_path != None: os.remove(ph_path)

#     elif "Animation" == msg_type:
#         try:
#             await client.send_animation(chat, file, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        

#     elif "Sticker" == msg_type:
#         try:
#             await client.send_sticker(chat, file, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        

#     elif "Voice" == msg_type:
#         try:
#             await client.send_voice(chat, file, caption=caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

#     elif "Audio" == msg_type:
#         try:
#             ph_path = await acc.download_media(msg.audio.thumbs[0].file_id)
#         except:
#             ph_path = None

#         try:
#             await client.send_audio(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])   
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        
#         if ph_path != None: os.remove(ph_path)

#     elif "Photo" == msg_type:
#         try:
#             await client.send_photo(chat, file, caption=caption, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
    
#     if os.path.exists(f'{message.id}upstatus.txt'): 
#         os.remove(f'{message.id}upstatus.txt')
#         os.remove(file)
#     await client.delete_messages(message.chat.id,[smsg.id])


# # get the type of message
# def get_message_type(msg: pyrogram.types.messages_and_media.message.Message):
#     try:
#         msg.document.file_id
#         return "Document"
#     except:
#         pass

#     try:
#         msg.video.file_id
#         return "Video"
#     except:
#         pass

#     try:
#         msg.animation.file_id
#         return "Animation"
#     except:
#         pass

#     try:
#         msg.sticker.file_id
#         return "Sticker"
#     except:
#         pass

#     try:
#         msg.voice.file_id
#         return "Voice"
#     except:
#         pass

#     try:
#         msg.audio.file_id
#         return "Audio"
#     except:
#         pass

#     try:
#         msg.photo.file_id
#         return "Photo"
#     except:
#         pass

#     try:
#         msg.text
#         return "Text"
#     except:
#         pass










# # Don't Remove Credit Tg - @VJ_Botz
# # Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# # Ask Doubt on telegram @KingVJ01

# import asyncio 
# import pyrogram
# from pyrogram import Client, filters
# from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 
# import time
# import math
# import os
# import threading
# import json
# from config import API_ID, API_HASH
# from database.db import database 
# from TechVJ.strings import strings, HELP_TXT

# def get(obj, key, default=None):
#     try:
#         return obj[key]
#     except:
#         return default

# # Helper for human readable bytes
# def humanbytes(size):
#     if not size:
#         return ""
#     power = 2**10
#     n = 0
#     Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
#     while size > power:
#         size /= power
#         n += 1
#     return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

# # Modified download status tracker
# async def downstatus(client: Client, statusfile, message):
#     while True:
#         if os.path.exists(statusfile):
#             break
#         await asyncio.sleep(3)
      
#     while os.path.exists(statusfile):
#         with open(statusfile, "r") as downread:
#             txt = downread.read()
#         try:
#             # Removed "Downloaded :" prefix because it's now in the progress text
#             await client.edit_message_text(message.chat.id, message.id, txt)
#             await asyncio.sleep(2) # Faster updates (2s instead of 10s)
#         except:
#             await asyncio.sleep(2)

# # Modified upload status tracker
# async def upstatus(client: Client, statusfile, message):
#     while True:
#         if os.path.exists(statusfile):
#             break
#         await asyncio.sleep(3)      
#     while os.path.exists(statusfile):
#         with open(statusfile, "r") as upread:
#             txt = upread.read()
#         try:
#             # Removed "Uploaded :" prefix because it's now in the progress text
#             await client.edit_message_text(message.chat.id, message.id, txt)
#             await asyncio.sleep(2) # Faster updates
#         except:
#             await asyncio.sleep(2)

# # Enhanced progress writer
# def progress(current, total, message, type, start_time):
#     now = time.time()
#     diff = now - start_time
    
#     # Calculate speed
#     if diff > 0:
#         speed = current / diff
#     else:
#         speed = 0
        
#     percentage = current * 100 / total
    
#     # 10-Block Progress Bar Logic
#     filled_blocks = math.floor(percentage / 10)
#     empty_blocks = 10 - filled_blocks
#     bar = "■" * filled_blocks + "□" * empty_blocks

#     # Determine label (Downloading vs Uploading) based on type
#     process_type = "Downloading" if type == "down" else "Uploading"

#     # Enhanced UI Text
#     text = f"""**{process_type}**
# {bar}
# **Percentage:** {percentage:.2f}%
# **Speed:** {humanbytes(speed)}/s
# **Done:** {humanbytes(current)} of {humanbytes(total)}"""

#     with open(f'{message.id}{type}status.txt', "w") as fileup:
#         fileup.write(text)

# # start command
# @Client.on_message(filters.command(["start"]))
# async def send_start(client: Client, message: Message):
#     buttons = [[
#         InlineKeyboardButton("𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭", url = "https://t.me/Farooq_is_King")
#     ],[
#         InlineKeyboardButton('🔍 WD Topic Group', url='https://t.me/Op_Topic_Group'),
#         InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Opleech_WD')
# 	]]
#     reply_markup = InlineKeyboardMarkup(buttons)
#     await client.send_message(message.chat.id, f"<b>👋 Hi {message.from_user.mention}, I am Save Restricted Content Bot, I can send you restricted content by its post link.\n\nFor downloading restricted content /login first.\n\nKnow how to use bot by - /help</b>", reply_markup=reply_markup, reply_to_message_id=message.id)
#     return

# # help command
# @Client.on_message(filters.command(["help"]))
# async def send_help(client: Client, message: Message):
#     await client.send_message(message.chat.id, f"{HELP_TXT}")

# @Client.on_message(filters.text & filters.private)
# async def save(client: Client, message: Message):
#     if "https://t.me/" in message.text:
#         datas = message.text.split("/")
#         temp = datas[-1].replace("?single","").split("-")
#         fromID = int(temp[0].strip())
#         try:
#             toID = int(temp[1].strip())
#         except:
#             toID = fromID
#         for msgid in range(fromID, toID+1):
#             # private
#             if "https://t.me/c/" in message.text:
#                 user_data = database.find_one({'chat_id': message.chat.id})
#                 if not get(user_data, 'logged_in', False) or user_data['session'] is None:
#                     await client.send_message(message.chat.id, strings['need_login'])
#                     return
#                 acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
#                 await acc.connect()
#                 chatid = int("-100" + datas[4])
#                 await handle_private(client, acc, message, chatid, msgid)
    
#             # bot
#             elif "https://t.me/b/" in message.text:
#                 user_data = database.find_one({"chat_id": message.chat.id})
#                 if not get(user_data, 'logged_in', False) or user_data['session'] is None:
#                     await client.send_message(message.chat.id, strings['need_login'])
#                     return
#                 acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
#                 await acc.connect()
#                 username = datas[4]
#                 try:
#                     await handle_private(client, acc, message, username, msgid)
#                 except Exception as e:
#                     await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            
# 	        # public
#             else:
#                 username = datas[3]

#                 try:
#                     msg = await client.get_messages(username, msgid)
#                 except UsernameNotOccupied: 
#                     await client.send_message(message.chat.id, "The username is not occupied by anyone", reply_to_message_id=message.id)
#                     return
#                 try:
#                     await client.copy_message(message.chat.id, msg.chat.id, msg.id, reply_to_message_id=message.id)
#                 except:
#                     try:    
#                         user_data = database.find_one({"chat_id": message.chat.id})
#                         if not get(user_data, 'logged_in', False) or user_data['session'] is None:
#                             await client.send_message(message.chat.id, strings['need_login'])
#                             return
#                         acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
#                         await acc.connect()
#                         await handle_private(client, acc, message, username, msgid)
                        
#                     except Exception as e:
#                         await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

#             # wait time
#             await asyncio.sleep(3)

# # handle private
# async def handle_private(client: Client, acc, message: Message, chatid: int, msgid: int):
#     msg: Message = await acc.get_messages(chatid, msgid)
#     msg_type = get_message_type(msg)
#     chat = message.chat.id
#     if "Text" == msg_type:
#         try:
#             await client.send_message(chat, msg.text, entities=msg.entities, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
#             return

#     smsg = await client.send_message(message.chat.id, 'Downloading', reply_to_message_id=message.id)
#     dosta = asyncio.create_task(downstatus(client, f'{message.id}downstatus.txt', smsg))
    
#     # Start timer for download
#     start_time = time.time()
    
#     try:
#         # Passed start_time to progress_args
#         file = await acc.download_media(msg, progress=progress, progress_args=[message, "down", start_time])
#         os.remove(f'{message.id}downstatus.txt')
        
#     except Exception as e:
#         await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)  
    
#     upsta = asyncio.create_task(upstatus(client, f'{message.id}upstatus.txt', smsg))

#     if msg.caption:
#         caption = msg.caption
#     else:
#         caption = None
    
#     # Reset timer for upload
#     start_time = time.time()

#     if "Document" == msg_type:
#         try:
#             ph_path = await acc.download_media(msg.document.thumbs[0].file_id)
#         except:
#             ph_path = None
        
#         try:
#             await client.send_document(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
#         if ph_path != None: os.remove(ph_path)
        

#     elif "Video" == msg_type:
#         try:
#             ph_path = await acc.download_media(msg.video.thumbs[0].file_id)
#         except:
#             ph_path = None
        
#         try:
#             await client.send_video(chat, file, duration=msg.video.duration, width=msg.video.width, height=msg.video.height, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
#         if ph_path != None: os.remove(ph_path)

#     elif "Animation" == msg_type:
#         try:
#             await client.send_animation(chat, file, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        

#     elif "Sticker" == msg_type:
#         try:
#             await client.send_sticker(chat, file, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        

#     elif "Voice" == msg_type:
#         try:
#             await client.send_voice(chat, file, caption=caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

#     elif "Audio" == msg_type:
#         try:
#             ph_path = await acc.download_media(msg.audio.thumbs[0].file_id)
#         except:
#             ph_path = None

#         try:
#             await client.send_audio(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])   
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        
#         if ph_path != None: os.remove(ph_path)

#     elif "Photo" == msg_type:
#         try:
#             await client.send_photo(chat, file, caption=caption, reply_to_message_id=message.id)
#         except Exception as e:
#             await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
    
#     if os.path.exists(f'{message.id}upstatus.txt'): 
#         os.remove(f'{message.id}upstatus.txt')
#         os.remove(file)
#     await client.delete_messages(message.chat.id,[smsg.id])

# # get the type of message
# def get_message_type(msg: pyrogram.types.messages_and_media.message.Message):
#     try:
#         msg.document.file_id
#         return "Document"
#     except:
#         pass

#     try:
#         msg.video.file_id
#         return "Video"
#     except:
#         pass

#     try:
#         msg.animation.file_id
#         return "Animation"
#     except:
#         pass

#     try:
#         msg.sticker.file_id
#         return "Sticker"
#     except:
#         pass

#     try:
#         msg.voice.file_id
#         return "Voice"
#     except:
#         pass

#     try:
#         msg.audio.file_id
#         return "Audio"
#     except:
#         pass

#     try:
#         msg.photo.file_id
#         return "Photo"
#     except:
#         pass

#     try:
#         msg.text
#         return "Text"
#     except:
#         pass

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio 
import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import time
import math
import os
from config import API_ID, API_HASH
from database.db import database 
from TechVJ.strings import strings, HELP_TXT

# Global Dictionary to track cancellation states
CANCEL_TASKS = {}

def get(obj, key, default=None):
    try:
        return obj[key]
    except:
        return default

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

async def downstatus(client: Client, statusfile, message):
    while True:
        if os.path.exists(statusfile):
            break
        await asyncio.sleep(3)
      
    while os.path.exists(statusfile):
        with open(statusfile, "r") as downread:
            txt = downread.read()
        try:
            await client.edit_message_text(message.chat.id, message.id, txt)
            await asyncio.sleep(2)
        except:
            await asyncio.sleep(2)

async def upstatus(client: Client, statusfile, message):
    while True:
        if os.path.exists(statusfile):
            break
        await asyncio.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile, "r") as upread:
            txt = upread.read()
        try:
            await client.edit_message_text(message.chat.id, message.id, txt)
            await asyncio.sleep(2)
        except:
            await asyncio.sleep(2)

def progress(current, total, message, type, start_time):
    now = time.time()
    diff = now - start_time
    if diff > 0:
        speed = current / diff
    else:
        speed = 0
    percentage = current * 100 / total
    filled_blocks = math.floor(percentage / 10)
    empty_blocks = 10 - filled_blocks
    bar = "■" * filled_blocks + "□" * empty_blocks
    process_type = "Downloading" if type == "down" else "Uploading"
    text = f"**{process_type}**\n{bar}\n**Percentage:** {percentage:.2f}%\n**Speed:** {humanbytes(speed)}/s\n**Done:** {humanbytes(current)} of {humanbytes(total)}"
    with open(f'{message.id}{type}status.txt', "w") as fileup:
        fileup.write(text)

# --- STOP BUTTON CALLBACK ---
@Client.on_callback_query(filters.regex("stop_batch"))
async def stop_batch_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    CANCEL_TASKS[chat_id] = True
    await callback_query.answer("Stopping batch process...", show_alert=True)
    await callback_query.message.edit_text("🛑 **Process Stopped by User.**")

@Client.on_message(filters.command(["start"]))
async def send_start(client: Client, message: Message):
    buttons = [[
        InlineKeyboardButton("𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭", url = "https://t.me/Farooq_is_King")
    ],[
        InlineKeyboardButton('🔍 WD Topic Group', url='https://t.me/Op_Topic_Group'),
        InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Opleech_WD')
	]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(message.chat.id, f"<b>👋 Hi {message.from_user.mention}, I am Save Restricted Content Bot, I can send you restricted content by its post link.\n\nFor downloading restricted content /login first.\n\nKnow how to use bot by - /help</b>", reply_markup=reply_markup, reply_to_message_id=message.id)

@Client.on_message(filters.command(["help"]))
async def send_help(client: Client, message: Message):
    await client.send_message(message.chat.id, f"{HELP_TXT}")

@Client.on_message(filters.command(["join"]))
async def join_channel(client: Client, message: Message):
    if len(message.command) < 2:
        await client.send_message(message.chat.id, "**Usage:** `/join https://t.me/+...`\n\nUse this to join private channels so the bot can access posts.")
        return

    invite_link = message.command[1]
    
    user_data = database.find_one({'chat_id': message.chat.id})
    if not get(user_data, 'logged_in', False) or user_data['session'] is None:
        await client.send_message(message.chat.id, strings['need_login'])
        return

    msg = await client.send_message(message.chat.id, "Attempting to join...")
    try:
        acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
        await acc.connect()
        try:
            await acc.join_chat(invite_link)
            await msg.edit("**Successfully joined the channel!** ✅\n\nYou can now send posts from this channel.")
        except UserAlreadyParticipant:
            await msg.edit("**You are already in this channel.**")
        except Exception as e:
            await msg.edit(f"**Failed to join:**\n`{e}`")
    except Exception as e:
        await msg.edit(f"**Session Error:**\n`{e}`")

@Client.on_message(filters.text & filters.private)
async def save(client: Client, message: Message):
    if "https://t.me/" in message.text:
        
        # 1. CRASH FIX: Check for invite links or non-post links
        if "t.me/+" in message.text or "joinchat" in message.text:
            return await client.send_message(message.chat.id, "**That looks like an invite link!**\nPlease use `/join <link>` to join the channel first.")
        
        # 2. Reset Cancel Flag
        CANCEL_TASKS[message.chat.id] = False

        datas = message.text.split("/")
        
        # 3. ROBUST PARSING (Prevents invalid literal int() error)
        try:
            temp = datas[-1].replace("?single","").split("-")
            fromID = int(temp[0].strip())
            try:
                toID = int(temp[1].strip())
            except:
                toID = fromID
        except ValueError:
            return await client.send_message(message.chat.id, "**Invalid Link Format.**\nPlease make sure you are sending a specific post link.")

        total_batch = toID - fromID + 1
        current_count = 0
        
        # 4. Stop Button Markup
        stop_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ Stop Batch", callback_data="stop_batch")]])
        
        batch_msg = await client.send_message(
            message.chat.id, 
            f"**Batch Progress:** 0/{total_batch}\nStarting...",
            reply_markup=stop_markup
        )

        for msgid in range(fromID, toID+1):
            
            # 5. Check Cancellation
            if CANCEL_TASKS.get(message.chat.id):
                break # Stop the loop

            current_count += 1
            try:
                await batch_msg.edit(
                    f"**Batch Progress:** {current_count}/{total_batch}\nProcessing ID: {msgid}",
                    reply_markup=stop_markup
                )
            except:
                pass

            if "https://t.me/c/" in message.text:
                user_data = database.find_one({'chat_id': message.chat.id})
                if not get(user_data, 'logged_in', False) or user_data['session'] is None:
                    await client.send_message(message.chat.id, strings['need_login'])
                    return
                
                try:
                    chatid = int("-100" + datas[4])
                except ValueError:
                    await client.send_message(message.chat.id, "**Error:** Could not determine Channel ID. Please check the link.")
                    return

                acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
                await acc.connect()
                await handle_private(client, acc, message, chatid, msgid)
            elif "https://t.me/b/" in message.text:
                user_data = database.find_one({"chat_id": message.chat.id})
                if not get(user_data, 'logged_in', False) or user_data['session'] is None:
                    await client.send_message(message.chat.id, strings['need_login'])
                    return
                acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
                await acc.connect()
                username = datas[4]
                try:
                    await handle_private(client, acc, message, username, msgid)
                except Exception as e:
                    await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            else:
                username = datas[3]
                try:
                    msg = await client.get_messages(username, msgid)
                except UsernameNotOccupied: 
                    await client.send_message(message.chat.id, "The username is not occupied by anyone", reply_to_message_id=message.id)
                    return
                try:
                    await client.copy_message(message.chat.id, msg.chat.id, msg.id, reply_to_message_id=message.id)
                except:
                    try:    
                        user_data = database.find_one({"chat_id": message.chat.id})
                        if not get(user_data, 'logged_in', False) or user_data['session'] is None:
                            await client.send_message(message.chat.id, strings['need_login'])
                            return
                        acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
                        await acc.connect()
                        await handle_private(client, acc, message, username, msgid)
                    except Exception as e:
                        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            await asyncio.sleep(3)
        
        # Cleanup
        if not CANCEL_TASKS.get(message.chat.id):
            try:
                await batch_msg.delete()
            except:
                pass
            await client.send_message(message.chat.id, "**Task Completed!** ✅")

async def handle_private(client: Client, acc, message: Message, chatid: int, msgid: int):
    # --- FIX FOR PEER ID INVALID ---
    try:
        # Try fetching message directly
        msg: Message = await acc.get_messages(chatid, msgid)
    except Exception as e:
        # If it fails (PeerIdInvalid), try to refresh the cache by fetching the chat info first
        try:
            await acc.get_chat(chatid)
            msg: Message = await acc.get_messages(chatid, msgid)
        except Exception as e2:
             await client.send_message(message.chat.id, f"**Error:** I can't access this channel even after retrying.\nPlease double-check if you are a member of this private channel.\nError: `{e2}`")
             return
    # -------------------------------

    msg_type = get_message_type(msg)
    chat = message.chat.id
    if "Text" == msg_type:
        try:
            await client.send_message(chat, msg.text, entities=msg.entities, reply_to_message_id=message.id)
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            return

    smsg = await client.send_message(message.chat.id, 'Downloading', reply_to_message_id=message.id)
    dosta = asyncio.create_task(downstatus(client, f'{message.id}downstatus.txt', smsg))
    start_time = time.time()
    try:
        file = await acc.download_media(msg, progress=progress, progress_args=[message, "down", start_time])
        os.remove(f'{message.id}downstatus.txt')
    except Exception as e:
        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)  
    
    upsta = asyncio.create_task(upstatus(client, f'{message.id}upstatus.txt', smsg))
    if msg.caption:
        caption = msg.caption
    else:
        caption = None
    start_time = time.time()

    if "Document" == msg_type:
        try:
            ph_path = await acc.download_media(msg.document.thumbs[0].file_id)
        except:
            ph_path = None
        try:
            await client.send_document(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        if ph_path != None: os.remove(ph_path)

    elif "Video" == msg_type:
        try:
            ph_path = await acc.download_media(msg.video.thumbs[0].file_id)
        except:
            ph_path = None
        try:
            await client.send_video(chat, file, duration=msg.video.duration, width=msg.video.width, height=msg.video.height, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        if ph_path != None: os.remove(ph_path)

    elif "Animation" == msg_type:
        try:
            await client.send_animation(chat, file, reply_to_message_id=message.id)
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

    elif "Sticker" == msg_type:
        try:
            await client.send_sticker(chat, file, reply_to_message_id=message.id)
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

    elif "Voice" == msg_type:
        try:
            await client.send_voice(chat, file, caption=caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

    elif "Audio" == msg_type:
        try:
            ph_path = await acc.download_media(msg.audio.thumbs[0].file_id)
        except:
            ph_path = None
        try:
            await client.send_audio(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message, "up", start_time])   
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        if ph_path != None: os.remove(ph_path)

    elif "Photo" == msg_type:
        try:
            await client.send_photo(chat, file, caption=caption, reply_to_message_id=message.id)
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
    
    if os.path.exists(f'{message.id}upstatus.txt'): 
        os.remove(f'{message.id}upstatus.txt')
        os.remove(file)
    await client.delete_messages(message.chat.id,[smsg.id])

def get_message_type(msg: pyrogram.types.messages_and_media.message.Message):
    if hasattr(msg, 'document') and msg.document: return "Document"
    if hasattr(msg, 'video') and msg.video: return "Video"
    if hasattr(msg, 'animation') and msg.animation: return "Animation"
    if hasattr(msg, 'sticker') and msg.sticker: return "Sticker"
    if hasattr(msg, 'voice') and msg.voice: return "Voice"
    if hasattr(msg, 'audio') and msg.audio: return "Audio"
    if hasattr(msg, 'photo') and msg.photo: return "Photo"
    if hasattr(msg, 'text') and msg.text: return "Text"
