from discord.ext.commands import Cog
from discord.ext.commands import command
import requests
from ..face_mirror import face_mirror

class FaceMirrorCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="shronk-left", aliases=["shrnkl"])
    async def shronk_left(self, ctx):
        attachment = ctx.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        await face_mirror.run(filename, 'left')

    @command(name="shronk-right", aliases=["shrnkr"])
    async def shronk_right(self, ctx):
        attachment = ctx.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        await face_mirror.run(filename, 'left')

    @command(name="Hi")
    async def hi(self, ctx):
        await ctx.send("Hello!")

def setup(bot):
    bot.add_cog(FaceMirrorCog(bot))