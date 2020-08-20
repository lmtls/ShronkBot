from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
PREFIX = '%'
OWNERIDS = [464482961488871436]

class Bot(BotBase):
    def __init__(self):
        self.guild = None
        self.PREFIX = PREFIX
        self.ready = False
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX, owner_ids=OWNERIDS)

    def run(self, version):
        self.VERSION = version
        with open('./lib/bot/token.0', 'r', encoding='utf-8') as tf:
            self.TOKEN = tf.read()

        print('bot running...')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('bot connected')

    async def on_disconnect(self):
        print('bot disconnected')
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(743554703086059601)
            print('bot ready')
        else:
            print('bot reconnected')

    async def on_message(self, message):
        pass

bot = Bot()