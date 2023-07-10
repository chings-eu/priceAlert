#import asyncio
import telegram

# Replace 'your_bot_token' with your own bot token
bot_token = '6252680814:AAGdwdO27on2fP5lg4gPCmLMIHvUAhLyW34'

# Replace 'your_chat_id' with the desired chat ID (group: bot test)
chat_id = '-908091973'

async def send_telegram_message(bot_token, chat_id, message):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

# # Create an event loop
# loop = asyncio.get_event_loop()
# # Send the message
# loop.run_until_complete(send_telegram_message(bot_token, chat_id, "hello world"))
# loop.run_until_complete(send_telegram_message(bot_token, chat_id, "hello world again"))

# # Close the event loop
# loop.close()