from telegram import Bot

class Erris:
    # ? inisialisasi bot
    def __init__(self, chat_id: str = None) -> None:
        BOT_TOKEN = '7352287207:AAGrFDiD8ucw-ANNGmP0rEJ_aaBdlKIfBVI'

        if chat_id is None:
            CHAT_ID = '6627739598'
        else:
            CHAT_ID = chat_id

        self.chat_id = CHAT_ID
        self.bot = Bot(token=BOT_TOKEN)
        
    # ? send message function
    async def send_message(self, message:str):
        await self.bot.send_message(chat_id=self.chat_id, text=message)

