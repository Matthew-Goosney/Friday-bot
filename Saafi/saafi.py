from discord.ext import commands
import discord

BOT_TOKEN = "NDI1Mzc1OTk3NTAwNTg4MDQ0.GW2cgQ.WnoNLz15RGEEnpoaHoQ0Q28CAKtP38mu_yIytA"
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