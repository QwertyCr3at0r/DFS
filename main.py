import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот запущен: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Понг! {round(bot.latency * 1000)}ms")

@bot.command()
async def привет(ctx):
    await ctx.send(f"Привет, {ctx.author.mention}!")

bot.run(os.environ["TOKEN"])
