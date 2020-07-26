import os
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(
        command_prefix='!',
        description='sample discord bot',
        case_insensitive=True    
    )

@bot.event
async def on_ready():
    print(f'{bot.user.mention} has connected to Discord!')

@bot.command()
async def hi(ctx):
    await ctx.send(f'{ctx.author.mention} Hi I am sample Discord BOT')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        msg_s = f"{ctx.author.mention} Invalid Command"
        await ctx.send(msg_s)
    else:
        raise error
bot.run(TOKEN)