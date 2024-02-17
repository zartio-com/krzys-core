import discord
from discord.ext import commands


class Krzys(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())
