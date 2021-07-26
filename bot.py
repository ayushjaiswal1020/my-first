from os import environ
from pyrogram import Client, filters



bot = Client('test bot',
             
             bot_token=1785476005:AAEoPNc1KjLf_TDquxSjyPgutN2dbZag2EE,
             workers=50,
             sleep_threshold=10)

@bot.on_message(filters.command('start'))
async def start(bot, message):
await message.reply(
        f"**𝗛𝗘𝗟𝗟𝗢🎈{message.chat.first_name}!**\n\n"
        "𝗜'𝗺 𝗹𝗶𝗻𝗸 Shortener 𝗯𝗼𝘁. 𝗝𝘂𝘀𝘁 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗹𝗶𝗻𝗸 𝗮𝗻𝗱 𝗴𝗲𝘁 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗱 𝗨𝗥𝗟. \n\n 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗕𝘆 @infozoxdesign💖")
bot.run()
