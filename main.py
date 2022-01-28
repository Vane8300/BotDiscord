import discord 
import os
import requests
import json

client = discord.Client()

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
  

  # if message.content.startswith("Buna"):
  #   await message.channel.send("A venit teroarea!!!")

  if message.content.startswith("$inspire"):
    quote = myFunctionAPI();
    await message.channel.send(quote)

    #whenever the bot notices that someone says $hello will response with the mess 
    # teroare

client.run(os.environ['TOKEN'])



