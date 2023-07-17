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
def get_msg(send_all=False):
    msg = ''
    for symbol in symbols.keys():
        print(symbol)
        current = round(get_current(symbol=symbol), 2)
        print(current)
        last = get_last_day(symbol=symbol)
        print(last)
        diff = current - last
        print(diff)
        perc = (diff / last) * 100
        perc = round(perc, 2)
        print(f'{perc} %')
        if send_all: # send all
            msg += f'{symbol} price ${current} changes: {perc} %\n'
        elif abs(perc) >= symbols[symbol]: # send only over threshold
            msg += f'{symbol} price ${current} changes: {perc} %\n'
    return msg

# since the task in pythonanywhere runs hourly, 
# for running more than once/hour, 
# this script should wait
import time
period = 60 * 60 # houly task
rounds = 10 # every (period / rounds) minutes
count = 0

# use a loop for the times
# check if it's from Mon. to Fri. and from UTC 13:30 - 20:00
# time nyse (north america) = utc-5
import time, pytz
time.utcnow()
local_time = time.localtime()
time_open = datetime.time(9, 30)
time_close = datetime.time(16, 0)
if day_current < 5 and datetime.time(13, 30) <= time_current <= datetime.time(22, 0):
    loop = asyncio.get_event_loop()
    while count < rounds:
        msg = ''
        try:
            # in the first hour, send all price
            if datetime.time(13, 30) <= time_current <= datetime.time(14, 15):
                msg = get_msg(True)
            # after first hour, only check when over the threshold
            else:
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