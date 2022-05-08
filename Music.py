import asyncio

import discord
from youtube_dl import YoutubeDL


class Music:
    def __init__(self):
        self.ctx = None
        self.voice = None

    async def start(self):
        await self.join()

    async def stop(self):
        try:
            self.voice.pause()
            await asyncio.sleep(1)
            await self.voice.disconnect()
        except AttributeError:
            await self.ctx.send("Der Bot ist in keinem Sprachkanal.")

    async def pause(self):
        self.voice.pause()
        await self.ctx.send("Paused")

    async def resume(self):
        self.voice.resume()
        await self.ctx.send("resume")

    async def play(self):
        if self.ctx.voice_client is None:
            await self.ctx.send("Der Bot war noch nicht in einem Sprachkanel, er versucht jetzt beizutreten.")
            await self.join()

        # self.ctx.voice_client.stop()

        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        ydl_option = {
            'format': "bestaudio"
        }
        url = self.ctx.message.content.split(" ")[2]

        with YoutubeDL(ydl_option) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)

            if self.ctx.voice_client.is_playing():  # Queue song bc bot is already playing.
                await self.ctx.send("Der Song ist in der Warteschlange!")
            else:  # Play song bc bot isn't playing.
                self.ctx.message.guild.voice_client.play(source)

    async def join(self):
        try:
            voice_channel = self.ctx.author.voice.channel

            if self.voice is None:
                await voice_channel.connect()
            else:
                await self.voice.move_to(voice_channel)
        except AttributeError:
            await self.ctx.send("Trete einen Sprachkanal bei, um den Bot zu dir zu rufen.")

    def update(self, ctx):
        self.ctx = ctx
        self.voice = ctx.message.guild.voice_client
        pass
