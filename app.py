
from telegram.ext import Updater, MessageHandler, Filters
 
from Adafruit_IO import Client
aio = Client('Pramodhreddyreddy','aio_hlfg38GJetkuohFWSHAH991X5PSY')
 
 
def pramodh1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned on')
  aio.send('light',1)
 
def pramodh2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned off')
  aio.send('light',0)
 
def pramodh3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')
  aio.send('light',2)
 
def pramodh4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')
  aio.send('light',3)
 
 
def main(bot,update):
  a= bot.message.text.lower()
  
  if a =="turn on light":
    pramodh1(bot,update)
  elif a =="turn off light":
    pramodh2(bot,update)
  elif a =="turn on fan":
    pramodh3(bot,update)
  elif a =="turn off fan":
    pramodh4(bot,update) 
     
 
bot_token = '1963401133:AAFMhkrJ7PQF0Fy99furV6dt4AStWMtMRwI'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()   
    
