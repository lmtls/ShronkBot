from discord.ext.commands import Bot as BotBase

import os
import requests
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
PREFIX = '~'
OWNERIDS = [464482961488871436]
COGS = [path.split('/')[-1][:-6] for path in glob("./lib/cogs/*cog.py")]

class Bot(BotBase):
    def __init__(self):
        self.guild = None
        self.PREFIX = PREFIX
        self.ready = False
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX, owner_ids=OWNERIDS)

    def setup(self):
        self.load_extension("lib.cogs.face_mirror_cog")
        print("face_mirror_cog loaded")

    def run(self, version):
        self.setup()
        print("running setup...")

        self.VERSION = version
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')

        print('running bot...')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('bot connected')

    async def on_disconnect(self):
        print('bot disconnected')

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            args[0].send("Error occured")
        await self.channel.send("Something went wrong")
    
    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(743554703086059601)
            self.channel = self.get_channel(743554703622668410)
            await self.channel.send('Bot Online!')
            print('bot ready')
        else:
            print('bot reconnected')

    async def on_message(self, message):
        if message.author.bot and message.author != message.guild.me:
            self.process_commands(message)

bot = Bot()