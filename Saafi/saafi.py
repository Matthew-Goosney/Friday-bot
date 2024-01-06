from discord.ext import commands
import discord

BOT_TOKEN = "NDI1Mzc1OTk3NTAwNTg4MDQ0.GGTy2f.y864YJPSz18uYlKKlNcGODK-9k6y3aIJx8eU3E"
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot is made")

@bot.event
async def on_message(message):
    message_content = message.content
    message_author = message_author
    print(f'New message -> {message_author} said: {message_content}')


bot.run(BOT_TOKEN)