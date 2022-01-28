import discord 
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

# py list with sad word
words = [
  "necajit", "trist", "suparat", "rau"
] 


# the msg that my bot send when somebody is not feeling well

starter_msg = [
  "Stiu ca poti!",
  "Baga tare!",
  "Mai e putin"
]

def myFunctionAPI():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_msg(message):
  if 'encouragements' in db.keys():
    encouragements = db['encouragements']
    encouragements.append(message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [message]

def delete_msg(index):
  # get the list from database
  encouragements = db['encouragements']
  if len[encouragements] > index:
    del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))


@client.event 
async def on_message(message):
  if (message.author == client.user):
    return

  msg = message.content

  if msg.startswith("$inspire"):
    quote = myFunctionAPI();
    await message.channel.send(quote)


  options = starter_msg

  if "encouragements" == db.keys():
    options = options + db['encouragements']

    #whenever the bot notices that someone says $hello will response with the mess 
    # teroare
  if any(word in msg for word in words):
    await message.channel.send(random.choice(options))


  if msg.startswith("$new"):
    encouragements_mess = msg.split("$new ", 1)[1]
    update_msg(encouragements_mess)
    await message.channel.send("New msj added")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_msg(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

keep_alive()
client.run(os.environ['TOKEN'])



