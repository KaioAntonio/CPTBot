import discord

client = discord.Client()

@client.event
async def on_ready():
    print("O BOT ESTÁ ONLINE")

@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention

    if(author == "CPTbot"):
        return

    if(content == "!play" and channel.name == "⭐𝐂𝐇𝐀𝐓"):
        await channel.send("ENVIE SOMENTE NO CHAT DE MUSICA " + mention)

    if (content == "bom dia" and channel.name == "⭐𝐂𝐇𝐀𝐓"):
        await channel.send("bom dia " + mention)

    if (content == "boa tarde" and channel.name == "⭐𝐂𝐇𝐀𝐓"):
        await channel.send("boa tarde " + mention)

    if (content == "boa noite" and channel.name == "⭐𝐂𝐇𝐀𝐓"):
        await channel.send("boa noite " + mention)

client.run("ODk1MDYyNjM0OTk3NjE2NjYx.YVzGCQ.Yfi18iHdIKAHwV7A68lyN2we188")



