 
 import os
 Active_Key = = os.getenv('Active_Key')
Username = = os.getenv('Username')
bot_token = os.getenv('bot_token')
from telegram.ext import Updater, MessageHandler, Filters
 
from Adafruit_IO import Client
aio = Client(Username,Active_key)
 
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
     
 
bot_token = bot_token
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()   
    
 
