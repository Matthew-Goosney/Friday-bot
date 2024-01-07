from discord.ext import commands
import discord
from jproperties import Properties


configs = Properties()    
with open("properties.properties", "rb") as config_file:
    configs.load(config_file)
    TOKEN = configs.get("TOKEN").data
    print(TOKEN)

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("bot is made")

@bot.event
async def on_message(message):
    message_content = message.content
    for word in swears:
        if word in message_content:
            print(word)
            await message.delete()
            await message.channel.send("Don't use that word!") 

bot.run(TOKEN)