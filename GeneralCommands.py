import asyncio
import discord
from discord import File
from discord.ext import commands
from discord.ext.commands import Context

FILEPATH = 'stats.log'

async def status_task(client):
    while True:
        await client.change_presence(activity=discord.Game('Python'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('Java'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('Javascript'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('C++'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('C#'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('HTML'), status=discord.Status.online)
        await asyncio.sleep(3)


async def upload_file(ctx: Context):
    messages = await ctx.channel.history().flatten()
    file = open(FILEPATH, 'w+')

    for msg in messages:
        file.write(str() + str(msg.author) + ": " + msg.content + "\n")

    await ctx.channel.send(file=discord.File(FILEPATH))


async def hello(ctx: Context):
    if ctx.author.bot:
        return
    await ctx.channel.send('Hallo {}'.format(ctx.author.mention))


async def pn(ctx: Context):
    if ctx.author.bot:
        return

    await ctx.author.send('HIHIHI. Ich hab dir geschieben :)')
