from discord.ext import commands
import discord
import asyncio

class maid_cog:

    def __init__(self, bot):
        self.bot = bot
        self.king = None


    async def on_ready(self):
        self.bot.loop.create_task(self.replyLoop())

    async def replyLoop(self):
        i= 0
        while(True):
            try:
                await self.bot.send_message(self.bot.get_channel(str(226771859964690432)), str(i) + " testing the length of my dong, you know what I am saying?")
                i+=1
                await asyncio.sleep(5.0)
            except:
                print("replyLoop error")
                self.bot.loop.create_task(self.replyLoop())
                break

def setup(bot):
    bot.add_cog(maid_cog(bot))