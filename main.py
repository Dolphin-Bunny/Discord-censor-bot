import discord

client = discord.Client()

@client.event
async def on_message(message):
    if not message.author.bot:
        fp=open('bad_words.txt')
        words=fp.read().split('\n')
        fp.close()
        for word in words:
            if word in message.content.split():
                await message.delete()
                await message.channel.send(message.author.mention+' your message was censored')

client.run("NzA1MTI1NjI2NzE3Mjc0MjAy.XqnKBA.MIi71fOMj1P5v887iB7uZxl7eAE")
