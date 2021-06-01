from typing import Sequence
import discord
from discord import channel
from discord import message
from discord.ext import commands
import discord, asyncio, random





token = "ODQxNjE1Mjk4MzI3MjE2MTQ5.YJpVUw.n0sniggmY9wNBO01NPBo12CXRnI" #봇토큰 설정
client = discord.Client()#client 설정

@client.event
async def on_ready():#봇이 준비되었을떄
    print("우봇 준비완료!")
    print(client.user)
    print("===========================")



@client.event
async def on_message(message):#사용자가 메세지를 입력했을떄
    if message.content == ";야 강동원":
        await message.channel.send("왜불러 차은우")

    if message.content.startswith(f";채널메세지"):# !채널메세지 <채널아이디> <메세지내용>
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content.startswith(";클린"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제완료!")

    if message.content == ";랜덤":
        await message.channel.send(random.randint(1, 10))
    

    if message.content == ";알림":
        await message.channel.send(f"{message.author.mention},10초가 지났어요!")

    if message.content == ";노래명령":
        embed = discord.Embed(colour=discord.Colour.red(), title="노래봇 명령어")
        embed.set_image(url="https://cdn.discordapp.com/attachments/836950601669673012/849176617381003284/song_bot.png")
        await message.channel.send(embed=embed)


    if message.content.startswith == ";소주":
        soju = int(message.content.split(" ")[1])
        
        await message.channel.send(f"{soju}병 드리겠습니다")

client.run(token) 