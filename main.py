import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from TestYoutubeAPI import *
intents = discord.Intents.all()
APIKEY = 'key'

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print("Ready Steady Go!")
    print("===================")
    try:
        sync = await bot.tree.sync()
        print(f'Synced {len(sync)} commands')
    except Exception as e:
        print(e)


@bot.tree.command(name='test')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hey {interaction.user.mention}!')

@bot.tree.command(name = 'trauma', description='Be ready 😈')
async def traumatize_me(interaction: discord.Interaction):
    num = randint(1,10)
    await interaction.response.send_message(file=discord.File(f'Trauma/{num}.jpg'))

@bot.tree.command(name = 'lightskin', description="Sin, Sin city wasn't made for you")
async def lightskin(interaction):
    await interaction.response.send_message(file=discord.File('download.jpg'))

@bot.tree.command(name = 'get-youtube-video', description="A world of surprises")
@app_commands.describe(message = "What video are you looking for?")
async def youtube(interaction, message:str):
    id_ = get_id_video(message)
    await interaction.response.send_message(f'https://www.youtube.com/watch?v={id_}')

bot.run(APIKEY)
