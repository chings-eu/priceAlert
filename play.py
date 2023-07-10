# if is open, check stock price every hour
from getCurrentPrice import get_current
from getHistoricalPrice import get_last_day
import datetime
from watchlist import symbols
import asyncio
from msgByTelegram import bot_token, chat_id, send_telegram_message

time_current = datetime.datetime.now().time()
day_current = datetime.datetime.now().weekday()

# check all listed once as a text message
def get_msg():
    msg = ''
    for symbol in symbols.keys():
        print(symbol)
        current = get_current(symbol=symbol)
        print(current)
        last = get_last_day(symbol=symbol)
        print(last)
        diff = current - last
        print(diff)
        perc = (diff / last) * 100
        perc = round(perc, 2)
        print(f'{perc} %')
        if abs(perc) >= symbols[symbol]:
            msg += f'{symbol} price changes: {perc} %\n'
    return msg

import time
period = 60 * 60 # houly task
rounds = 10 # every (period / rounds) minutes
count = 0

# use a loop for the times
# check if it's from Mon. to Fri. and from UTC 13:30 - 20:00
if day_current < 5 and datetime.time(13, 30) <= time_current <= datetime.time(22, 0):
    loop = asyncio.get_event_loop()
    while count < rounds:
        msg = ''
        try:
            msg = get_msg()
            if msg == '':
                print('no message gathered')
            else:
                loop.run_until_complete(send_telegram_message(bot_token, chat_id, msg))
                time.sleep(period / rounds)
        except:
            print('Something went wrong. Check get_msg()')

        count += 1
    loop.close()
    print("message sending loop is done.")
else:
    print("nyse not in opening hour.")