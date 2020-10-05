# import os
# os.system('/usr/local/bin/python -m pip install --upgrade pip')
# os.system("TMPDIR=/home/container/tmp pip install --cache-dir=/home/container/tmp --build /home/container/tmp opencv-python")
# os.system("pip freeze")

from lib.bot import bot

VERSION = '0.0.1'

bot.run(VERSION)