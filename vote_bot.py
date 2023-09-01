import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

recent_poll_message = None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def start_vote(ctx, *options):
    # Split the options using commas
    await ctx.send("What will be the title for the poll?")
    question_input = await bot.wait_for('message')

    await ctx.send("Type in all of the options (Seperate each with a comma)")
    options_input = await bot.wait_for('message')

    question = question_input.content
    question.replace(" ", "")
    options = options_input.content.split(',')

    # Create a poll
    poll_embed = discord.Embed(
        title=f'🗳️ {question}', color=discord.Color.blue()
    )

    for i, option in enumerate(options, start=1):
        poll_embed.add_field(
            name=f'Option {i}', value=option.strip(), inline=False
        )

    poll_message = await ctx.send(embed=poll_embed)

    # Add reaction options
    for i in range(len(options)):
        # Unicode regional indicator symbols A-Z
        await poll_message.add_reaction(chr(0x1f1e6 + i))

    global recent_poll_message
    recent_poll_message = poll_message


@bot.command()
async def close_vote(ctx):
    global recent_poll_message

    async for message in ctx.channel.history(limit=50):
        if message.author == bot.user:
            poll_message = message
            break

    if recent_poll_message is None:
        await ctx.send("No recent poll message found in this channel.")
        return

    reactions = poll_message.reactions
    results = []

    for reaction in reactions:
        results.append(f'{reaction.emoji}: {reaction.count - 1} votes')

    results_embed = discord.Embed(
        title='📊 Voting Results', color=discord.Color.green()
    )

    results_embed.description = '\n'.join(results)
    await ctx.send(embed=results_embed)

    recent_poll_message = None

bot.run(DISCORD_TOKEN)
