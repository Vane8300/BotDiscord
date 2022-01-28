import discord 
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

# py list with sad word
words = [
  "necajit", "trist", "suparat", "rau", "stresat"
] 

# the msg that my bot send when somebody is not feeling well

starter_msg = [
  "Stiu ca poti!",
  "Baga tare!",
  "Mai e putin",
  "Baga o bere"
]

# my bot will response at a person that is sad with a motivational guotes

def myFunctionAPI():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


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

    #whenever the bot notices that someone says $hello will response with the mess 
    # teroare
  if any(word in msg for word in words):
    await message.channel.send(random.choice(starter_msg))

keep_alive()
client.run(os.environ['TOKEN'])



