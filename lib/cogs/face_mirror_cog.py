from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.message import File
import requests
from ..face_mirror import face_mirror

class FaceMirrorCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        print("cog ready")

    @command(name="shronk-left", aliases=["shrnkl", "shrl"])
    async def shronk_left(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalface_default.xml", 'left')
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")
            await ctx.send(file=File(f'./data/images/final/{final_filename}'))
        else:
            await ctx.send("No faces found")
        face_mirror.clear()

    @command(name="shronk-right", aliases=["shrnkr", "shrr"])
    async def shronk_right(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalface_default.xml", 'right')
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")
            await ctx.send(file=File(f'./data/images/final/{final_filename}'))
        else:
            await ctx.send("No faces found")
        face_mirror.clear()

    @command(name="shrlneko")
    async def shronk_cat_left(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalcatface.xml", 'left')
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")
            await ctx.send(file=File(f'./data/images/final/{final_filename}'))
        else:
            await ctx.send("No faces found")
        face_mirror.clear()

    @command(name="shrrneko")
    async def shronk_cat_right(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalcatface.xml", 'right')
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")
            await ctx.send(file=File(f'./data/images/final/{final_filename}'))
        else:
            await ctx.send("No faces found")
        face_mirror.clear()
        
    @command(name="shrlweeb")
    async def shronk_anime_left(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/lbpcascade_animeface.xml", 'left')
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")
            await ctx.send(file=File(f'./data/images/final/{final_filename}'))
        else:
            await ctx.send("No faces found")
        face_mirror.clear()
        
    @command(name="shrrweeb")
    async def shronk_anime_right(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/lbpcascade_animeface.xml", 'right')
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")
            await ctx.send(file=File(f'./data/images/final/{final_filename}'))
        else:
            await ctx.send("No faces found")
        face_mirror.clear()

def setup(bot):
    bot.add_cog(FaceMirrorCog(bot))