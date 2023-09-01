import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.typing = False

client = discord.Client(intents=intents)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content == '$inspire':
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$greet'):
        channel = message.channel
        msg = await client.wait_for('message')
        await channel.send(f'Hello {msg.author}!')

client.run(DISCORD_TOKEN)
