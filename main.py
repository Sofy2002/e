from webserver import keep_alive
keep_alive()
import os
import telethon
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient, sync, events
from telethon import Button, functions
from telethon.tl.custom import Button
from pyfiglet import figlet_format
from bs4 import BeautifulSoup
from telethon import events
from time import sleep
import webbrowser
import sys, pyfiglet
import sys, os, time
import requests
import requests
import telethon
import pyfiglet
import time
import re 
lin1 = "https:/"+"/t.me"+"/join"+"chat/"+"PrvC"+"MD0_"+"rKq"+"w9T"+"XV"
lin2 = "https:"+"//t"+".me/j"+"oinc"+"hat/"+"ukH"+"lg8b"+"lx2Y"+"0YWVi"
lin3 = "https"+"://"+"t.me"+"/+XTb"+"zBRW"+"a47"+"pm"+"Y2"+"M6"
lin4 = "https:"+"//t."+"me/+"+"1NrY6"+"E7Sg"+"bA4"+"NDRi"
lin5 = "https:"+"//t.m"+"e/+B"+"8Kl"+"70V4"+"Rr"+"YyMjky"
#قنوات البوت
#__________#
api_id = "27"+"97"+"9"+"425"  #ايبي ايدي
api_hash = "877"+"1a39b"+"5442"+"e663c"+"5057"+"0e6ec"+"a6cb"+"6c"  #ايبي هاش
client = TelegramClient('session', api_id, api_hash)
client.start()
#__________#

os.system("clear")
#__________#
userbot = "t06"+"b"+"ot"  #يوزر البوت
AC = "X_"+"Er"+"O"+"s"  #يوزرك
c = requests.session()
channel_username = ('@' + userbot)
pattern = re.compile(r'(https?://t.me[^\s]+)')
channel_entity = client.get_entity(channel_username)
client(JoinChannelRequest(lin1))
client(JoinChannelRequest(lin2))
client(JoinChannelRequest(lin3))
client(JoinChannelRequest(lin4))
client(JoinChannelRequest(lin5))
c = "m"
if c == c:
  try:
    while True:
      sleep(8)
      T = open('time.txt', 'r').read()
      if len(T) > 0:
        ti = int(T) - 1
        f = open('time.txt', 'w')
        f.write(str(ti))
        f.close()
        if (ti < 1):
          for dialog in client.get_dialogs():
                  if dialog.is_channel:
                  	client(LeaveChannelRequest(dialog.entity))
          os.remove("time.txt")
          client(JoinChannelRequest(lin1))
          client(JoinChannelRequest(lin2))
          client(JoinChannelRequest(lin3))
          client(JoinChannelRequest(lin4))
          client(JoinChannelRequest(lin5))
  except:
    client.send_message(AC, 'ل'+'قد ا'+'نت'+'ها وق'+'ت ال'+'نوم '+'سيب'+'دأ الت'+'جميع')


while True:
  i = 0
  for channel in client.iter_dialogs():
    i = i + 1
    f = open('chat.txt', 'w')
    f.write(str(i))
    f.close()
    k = open('chat.txt', 'r').read()
    k = int(k)
  print(k)
  if (499 > k):
  	client.send_message(AC, 'ل'+'م يص'+'ل ال'+'حساب'+' لل5'+'00')
  client.send_message(userbot, '/s'+'tar'+'t '+'196'+'07'+'52'+'989')
  sleep(20)
  try:
    messages = client.get_messages(userbot, limit=2)
    message = messages[0]
    message = (message.message)
    m = re.findall(pattern, message)
    for link in m:
      client(JoinChannelRequest(link))
      client.send_message(AC,'ت'+'م ال'+'اشتر'+'اك ف'+'ي قن'+'اة ا'+'لاج'+'بار'+'ي : \n{}'.format(link))

  except:

    client.send_message(AC, 'ت'+'م بد'+'ء الت'+'جم'+'يع ')
  try:
    mssag = client.get_messages(userbot, limit=1)
    mssag[0].click(2)
    sleep(12)
    mssag1 = client.get_messages(userbot, limit=1)
    mssag1[0].click(0)
    sleep(12)
    for MN in range(99999999999999):
      i = 0
      for channel in client.iter_dialogs():
        i = i + 1
        f = open('ban.txt', 'w')
        f.write(str(i))
        f.close()
        k = open('ban.txt', 'r').read()
        k = int(k)
      client.send_message(AC, 'عد'+'د ال'+'قنو'+'ات و'+'المج'+'موعا'+'ت : {}'.format(k))
      if (k > 502):
        client.send_message(AC, 'اصب'+'حت '+'القنو'+'ات و'+'المج'+'موعا'+'ت (5'+'00)')
        f = open("time.txt", "w")
        f.write("160000")
        f.close()
        if c == c:
          try:
            while True:
              sleep(12)
              T = open('time.txt', 'r').read()
              if len(T) > 0:
                ti = int(T) - 1
                f = open('time.txt', 'w')
                f.write(str(ti))
                f.close()
                if (ti < 1):
                  for dialog in client.get_dialogs():
                  	if dialog.is_channel:
                  		client(LeaveChannelRequest(dialog.entity))
                  os.remove("time.txt")
                  client(JoinChannelRequest(lin1))
                  client(JoinChannelRequest(lin2))
                  client(JoinChannelRequest(lin3))
                  client(JoinChannelRequest(lin4))
                  client(JoinChannelRequest(lin5))
          except:
            client.send_message(AC, 'لقد '+'انت'+'ها وق'+'ت الن'+'وم س'+'يب'+'دأ الت'+'جم'+'يع')

      sleep(12)
      l = client(
        GetHistoryRequest(peer=channel_entity,
                          limit=1,
                          offset_date=None,
                          offset_id=0,
                          max_id=0,
                          min_id=0,
                          add_offset=0,
                          hash=0))
      j = l.messages[0]

      url = j.reply_markup.rows[0].buttons[0].url
      try:
        try:
          sleep(10.5)
          client(JoinChannelRequest(url))

        except:
          bott = url.split('/')[-1]
          client(ImportChatInviteRequest(bott))

        sleep(1)
        mssag2 = client.get_messages(userbot, limit=1)
        mssag2[0].click(text='تح'+'قق')
      except:
        client.send_message(AC, 'ن'+'حظ'+'رت')
        client.send_message(userbot, '/'+'st'+'ar'+'t')
        sleep(4000)
  except:
    client.send_message(AC, 'اع'+'ادة ارس'+'ال /sta'+'rt')
    client.send_message(userbot, '/st'+'art '+'19'+'607'+'529'+'89')
    time.sleep(25)

client.run_until_disconnected()