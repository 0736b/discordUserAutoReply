from webserver import keep_alive
import os
#!/usr/bin/python
#-*-coding: utf-8 -*-
#-*-coding: utf-8 -*-
import discord #Discord API
import time

client = discord.Client()

answer = ""

@client.event
async def on_ready():
    print('ล็อคอินด้วย Token สำเร็จ User ของคุณคือ: {0.user}'.format(client))

@client.event
async def on_message(message):
    #Edit message at here
    if 'here' in message.content and message.author.id == hereIsID:
        print('ได้รับข้อความ A MEGALODON HAS SPAWNED IN THE RIVER')
        time.sleep(3)
        await message.channel.send('FISH') #This is message that reply when get event
        print('ส่งข้อความ FISH สำเร็จ')
        answer = "fish"
        return answer

    elif 'here' in message.content and message.author.id == hereIsID:
        print('ได้รับข้อความ IT''S RAINING COINS')
        time.sleep(3)
        await message.channel.send('CATCH') #This is message that reply when get event
        print('ส่งข้อความ CATCH สำเร็จ')
        answer = "catch"
        return answer

    elif 'here' in message.content and message.author.id == hereIsID:
        print('ได้รับข้อความ AN EPIC TREE HAS JUST GROWN')
        time.sleep(3)
        await message.channel.send('CHOP') #This is message that reply when get event
        print('ส่งข้อความ CHOP สำเร็จ')
        answer = "chop"
        return answer
        
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN, bot=False)
