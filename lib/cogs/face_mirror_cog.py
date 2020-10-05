from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.message import File
import requests
from ..face_mirror import face_mirror

class FaceMirrorCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        print("cog ready")

    @command(name="shronk", aliases=["shrnk"]) #flips human faces
    async def shronk(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalface_default.xml", "left")
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")           
            img_left = File(f"./data/images/final/{final_filename}")
            await ctx.send(file=img_left)         
            final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalface_default.xml", "right")
            img_right = File(f"./data/images/final/{final_filename}") 
            await ctx.send(file=img_right)
        else:
            await ctx.send("No faces found") 
        face_mirror.clear()

    @command(name="shronk_cat", aliases=["shrneko"]) #flips cat faces
    async def shronk_cat(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalcatface.xml", "left")
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")           
            img_left = File(f"./data/images/final/{final_filename}")
            await ctx.send(file=img_left)         
            final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/haarcascade_frontalcatface.xml", "right")
            img_right = File(f"./data/images/final/{final_filename}") 
            await ctx.send(file=img_right)
        else:
            await ctx.send("No faces found") 
        face_mirror.clear()
        
    @command(name="shronk_anime", aliases=["shrweeb"]) #flips anime faces
    async def shronk_cat(self, ctx):
        attachment = ctx.message.attachments[0]
        filename = attachment.filename
        url = attachment.url
        response = requests.get(url)
        file = open(f"./data/images/stock/{filename}", "wb")
        file.write(response.content)
        file.close()
        final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/lbpcascade_animeface.xml", "left")
        if face_count > 0:
            await ctx.send(f"{face_count} faces found")           
            img_left = File(f"./data/images/final/{final_filename}")
            await ctx.send(file=img_left)         
            final_filename, face_count = face_mirror.run(filename, "./lib/face_mirror/lbpcascade_animeface.xml", "right")
            img_right = File(f"./data/images/final/{final_filename}") 
            await ctx.send(file=img_right)
        else:
            await ctx.send("No faces found") 
        face_mirror.clear()
    
def setup(bot):
    bot.add_cog(FaceMirrorCog(bot))