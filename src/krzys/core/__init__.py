import argparse
import os
from importlib.metadata import entry_points
import discord
from discord.ext import commands

from .plugin import Plugin
from .config import *

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

krzys_path = os.path.expanduser('~/.krzys')
krzys_tmp_path = os.path.expanduser('~/.krzys/tmp')
if not os.path.exists(krzys_path):
    os.makedirs(krzys_path, exist_ok=True)

if not os.path.exists(krzys_tmp_path):
    os.makedirs(krzys_tmp_path, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument('--token', '-t',
                    type=str,
                    help='Discord bot token, defaults to env KRZYS_BOT_TOKEN',
                    default=os.getenv('KRZYS_BOT_TOKEN') or '')

args = parser.parse_args()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self):
        plugin_eps = entry_points(group="krzys.plugins")
        for plugin_ep in plugin_eps:
            print("Loading plugin:", plugin_ep.name)
            bot_plugin: Plugin = plugin_ep.load()(self)
            await bot_plugin.load()

    async def on_ready(self):
        await self.tree.sync()


def run():
    bot = Bot()
    bot.run(args.token)
