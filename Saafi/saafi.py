from discord.ext import commands
import discord

BOT_TOKEN = "MTE5MzI3NzQ4NjUxMTk2MDEwNA.Gl7Lhb.bMZdNyLrXWa1nYuQ0zpD-UN0RVQIJi4jS0sZGE"
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

with open('./constantSwears.txt', 'r') as f:
    global swears
    words = f.read()
    swears = words.split()

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
    await bot.process_commands(message)
    

bot.run(BOT_TOKEN)