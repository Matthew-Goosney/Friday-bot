from discord.ext import commands
import discord

BOT_TOKEN = "NDI1Mzc1OTk3NTAwNTg4MDQ0.GGTy2f.y864YJPSz18uYlKKlNcGODK-9k6y3aIJx8eU3E"
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

with open('constantSwears.txt', 'r') as f:
    global swears
    words = f.read()
    swears = words.split()

@bot.event
async def on_ready():
    print("bot is made")

@bot.event
async def on_message(ctx, message):
    message_content = message.content
    for word in swears:
        if word in message_content:
            await message.delete()
            await ctx.send("Dont use that word!")
    await ctx.process_message(message)
    

bot.run(BOT_TOKEN)