from discord.ext import commands
import discord

BOT_TOKEN = "NDI1Mzc1OTk3NTAwNTg4MDQ0.GepsGZ.-gcWUM3t17DMVJfyz3qFSaaa-vR0T2yD-gJcRQ"
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot is made")

@bot.command()
async def count(ctx, user: discord.Member, word):
    counter = 0
    async for message in ctx.history():
        if str(message.author) == str(user.name):
            if word.lower() in message.content.lower():
                counter += 1


@bot.command()
async def CountNWord(ctx, user: discord.Member):
    counter = 0
    nonowords = ["nigga", "nigger", "niggers"]
    async for message in ctx.history():
        if str(message.author) == str(user.name):
            if any(x in str(message.content).lower() for x in nonowords):
                counter += 1

    if counter == 0:
         await ctx.send(f"{user.mention} has never said the N-word. Good boy")
    else:
        await ctx.send(f"{user.mention} has said the N-word {counter} times. What a kerping racist!")

bot.run(BOT_TOKEN)