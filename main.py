# # Don't Remove Credit Tg - @VJ_Botz
# # Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# # Ask Doubt on telegram @KingVJ01

# from pyrogram import Client
# from config import API_ID, API_HASH, BOT_TOKEN

# class Bot(Client):

#     def __init__(self):
#         super().__init__(
#             "techvj login",
#             api_id=API_ID,
#             api_hash=API_HASH,
#             bot_token=BOT_TOKEN,
#             plugins=dict(root="TechVJ"),
#             workers=50,
#             sleep_threshold=10
#         )

      
#     async def start(self):
            
#         await super().start()
#         print('✔️ Bot Started Modified By 𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭')

#     async def stop(self, *args):

#         await super().stop()
#         print('Bot Stopped Bye')

# # Don't Remove Credit Tg - @VJ_Botz
# # Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# # Ask Doubt on telegram @KingVJ01









##########################################################



# main.py
# Don't Remove Credit Ig - @VJ_Botz

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import idle

app = Client(
    "techvj_login",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="TechVJ"),
    workers=10,
    sleep_threshold=10
)

def main():
    app.start()
    print("✅ Bot Started")
    idle()
    app.stop()
    print("❌ Bot Stopped")

if __name__ == "__main__":
    main()
