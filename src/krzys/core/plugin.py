from discord.ext import commands


class Plugin:
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    async def load(self):
        pass
