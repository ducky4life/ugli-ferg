# region setup
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

bot_prefix = "smort"

token = os.getenv("ROBO_TOKEN")

client = commands.Bot(
    command_prefix=[f"!{bot_prefix} "],
    intents=intents)

@client.event
async def on_ready():
    print('Roboduck is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ITS UGLI FERG!"))
    await client.tree.sync()
# endregion


async def send_codeblock(ctx, msg, *, view=None):
    if len(msg) > 1993:
        if len(msg) > 3993:
            first_msg = msg[:1993]
            second_msg = msg[1993:3987]
            third_msg = msg[3987:].strip()
            await ctx.send(f"```{first_msg}```")
            await ctx.send(f"```{second_msg}```")
            await ctx.send(f"```{third_msg}```")
        else:
            first_msg = msg[:1993]
            second_msg = msg[1993:].strip()
            await ctx.send(f"```{first_msg}```")
            await ctx.send(f"```{second_msg}```")
    else:
        await ctx.send(f"```{msg}```", view=view)

bot_id_list = [1186326404267266059, 839794863591260182, 944245571714170930, 1396935480284680334]

@client.event
async def on_message(message: discord.Message):
    await client.process_commands(message)
    if message.author.id not in bot_id_list and message.author.id:
        if "baa" in message.content.lower():
            await message.channel.send("Baaaaaaaa!")

@client.event
async def on_command_error(ctx, error):
    channel_id = 1131914463277240361
    channel = client.get_channel(channel_id)
    await channel.send(error)
    await channel.send(error.__traceback__)

client.run(token)
