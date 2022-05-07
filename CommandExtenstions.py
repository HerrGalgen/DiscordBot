import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord import Member
import GeneralCommands
from Music import Music

client = commands.Bot(
    command_prefix='-',
    help_command=None
)


@client.event
async def on_ready():
    print("Wir sind eingeloggt als {}".format(client.user.name))
    client.loop.create_task(GeneralCommands.status_task(client))


@client.command(
    name="stats",
    aliases=["f"],
    description="Sendet die geschriebenen Nachrichten als Datei an dich.",
    help="stats"
)
async def stats(ctx: Context):
    await GeneralCommands.upload_file(ctx)


@client.command(
    name="private",
    aliases=["pn"],
    description="Sendet dir eine private Nachricht.",
    help="pn"
)
async def private(ctx: Context):
    await GeneralCommands.pn(ctx)


@client.command(
    name="hello",
    aliases=["hi"],
    description="Sendet dir ein Hallo zurück.",
    help="hello"
)
async def hello(ctx: Context):
    await GeneralCommands.hello(ctx)


@client.command(
    name="music",
    aliases=["m"],
    description="Spielt Musik ab.",
    help="play"
)
async def play(ctx: Context):

    mode = ""
    music = Music(ctx)

    try:
        mode = ctx.message.content.split(" ")[1]
    except IndexError:
        await ctx.send("Bitte gib ein Argument an.")
        return None

    if mode == "start":
        await music.start()
    elif mode == "stop":
        await music.stop()
    elif mode == "play":
        await music.play()
    elif mode == "pause":
        await music.pause()
    elif mode == "resume":
        await music.resume()


if __name__ == "__main__":
    client.run('ODM1NTQ0MjY4MDU5MzEyMTg4.YIQ_PQ.dmhZVQMkhliP1U0KcsubQUoC9f0')
