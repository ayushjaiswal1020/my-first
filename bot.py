from os import environ
from pyrogram import Client, filters



bot = Client('test bot',
             api_id=3646731,
             api_hash='6e679b44365774a91173a9c45cac3b2a',
             bot_token='1785476005:AAEoPNc1KjLf_TDquxSjyPgutN2dbZag2EE',
             workers=50,
             sleep_threshold=10)

@bot.on_message(filters.command('start'))
async def start(bot, message):
await message.reply(
        f"**๐๐๐๐๐ข๐{message.chat.first_name}!**\n\n"
        "๐'๐บ ๐น๐ถ๐ป๐ธ Shortener ๐ฏ๐ผ๐. ๐๐๐๐ ๐๐ฒ๐ป๐ฑ ๐บ๐ฒ ๐น๐ถ๐ป๐ธ ๐ฎ๐ป๐ฑ ๐ด๐ฒ๐ ๐ฆ๐ต๐ผ๐ฟ๐๐ฒ๐ป๐ฒ๐ฑ ๐จ๐ฅ๐. \n\n ๐ง๐ต๐ถ๐ ๐๐ผ๐ ๐๐ ๐ ๐ฎ๐ฑ๐ฒ ๐๐ @infozoxdesign๐")
bot.run()
