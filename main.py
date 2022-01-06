import discord
import random
import responses

my_secret = 'TOKEN'
client = discord.Client()

predictions_8ball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.",
                     "You may rely on it.",
                     "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                     "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                     "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                     "Outlook not so good.", "Very doubtful."]

def rand_8ball():
    random_8ball = random.choice(predictions_8ball)
    print(random_8ball)
    return random_8ball


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$8ball"):
        await message.channel.send(rand_8ball())


client.run(my_secret)
