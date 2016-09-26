from discord.ext import commands
import discord
import asyncio

class maid_cog:

    def __init__(self, bot):
        self.bot = bot
        self.king = None
        self.initialized = False;


    async def on_ready(self):
        if(not initialized):
            self.bot.loop.create_task(self.replyLoop())
            self.bot.loop.create_task(self.progressLoop())
            initialized = True

    async def replyLoop(self):
        i= 0
        print(str(self.bot.user) + " has Entered the reply loop!\n")
        while(True):
            try:
                await self.bot.send_message(self.bot.get_channel(str(226771859964690432)), str(i) + " testing the length of my dong, you know what I am saying?")
                i+=1
                await asyncio.sleep(10.2)
            except:
                print("replyLoop error")
                self.bot.loop.create_task(self.replyLoop())
                break
        print("\n\n\n\n" + str(self.bot.user) + " has broken out of the reply loop!\n\n\n\n")

    async def progressLoop(self):
        while(True):
            try:
                await self.bot.send_message(self.bot.get_channel(str(226777134721531904)),"t!rank")
                if(self.king):
                    await self.bot.send_message(self.bot.get_channel(str(226804409659686913)), "t!rep " + self.king)
                    await self.bot.send_message(self.bot.get_channel(str(226804409659686913)), "t!daily " + self.king)
                await asyncio.sleep(1800)
            except:
                print("progressLoop error:")
                self.bot.loop.create_task(self.progressLoop())
                break


    async def on_message(self, message):
        if message.content == 'make me king':
            self.king = message.author.mention
            print(self.king + " is now King")
        if message.author == self.bot.user:
            await self.bot.delete_message(message)

def setup(bot):
    bot.add_cog(maid_cog(bot))