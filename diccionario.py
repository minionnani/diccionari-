import discord

from discord.ext import commands

# Prefijo del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name = 'saludar')
async def saludar(ctx):
    await ctx.send("Bienvenida gaby✨")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    #"""Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run('')
