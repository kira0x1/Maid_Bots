from discord.ext import commands
import discord
import asyncio
from bs4 import BeautifulSoup
import requests
import urllib.request
import random
import time

from cleverbot import Cleverbot

class maid_cog:
    "Fun commands"

    #woop woop

    def __init__(self, bot):
        self.bot = bot
        self.cb = Cleverbot()
        self.commentList = []
        print(len(self.commentList))
        self.previousTime = time.time()
        self.cd = 0.0
        self.initialized = False;
        self.beenSaid = []
        self.king = None


    async def on_ready(self):
        self.bot.loop.create_task(self.replyLoop())
        self.bot.loop.create_task(self.progressLoop())

    async def replyLoop(self):
        i= 0
        while(True):
            #if (len(self.commentList) > 0):
            await self.bot.send_message(self.bot.get_channel(str(226771859964690432)), (str(i)))
            i+=1
                #self.commentList.pop()
            await asyncio.sleep(3.0)

    async def progressLoop(self):
        while(True):
            await self.bot.send_message(self.bot.get_channel(str(226777134721531904)),"t!rank")
            if(self.king):
                await self.bot.send_message(self.bot.get_channel(str(226804409659686913)), "t!rep " + self.king)
                await self.bot.send_message(self.bot.get_channel(str(226804409659686913)), "t!daily " + self.king)
            await asyncio.sleep(600)


    async def on_message(self, message):
        if message.content == 'make me king':
            self.king = message.author.mention
            print(self.king + " is now King")
        if message.author == self.bot.user:
            await self.bot.delete_message(message)




def setup(bot):
    bot.add_cog(maid_cog(bot))