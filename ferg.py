# region setup
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from html2image import Html2Image
import time

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

bot_prefix = "ferg"
output_path = "images"

token = os.getenv("FERG_TOKEN")
hti = Html2Image(
    output_path=output_path,
    custom_flags=['--virtual-time-budget=10000', '--hide-scrollbars', '--default-background-color=00000000'],
)

if not os.path.exists(output_path):
    os.makedirs(output_path)

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


@client.hybrid_command()
async def load_html(ctx, *, html: str):
    curr_time = int(time.time())
    hti.screenshot(html_str=html, css_str="", save_as=f'{curr_time}.png')
    await ctx.send("ok", file=discord.File(f'{output_path}/{curr_time}.png'))

@client.hybrid_command()
async def load_html_url(ctx, url: str):
    curr_time = int(time.time())
    hti.screenshot(url=url, save_as=f'{curr_time}.png')
    await ctx.send("ok", file=discord.File(f'{output_path}/{curr_time}.png'))

@client.hybrid_command()
async def load_html_file(ctx, html_file: discord.Attachment):
    await html_file.save()
    curr_time = int(time.time())
    hti.screenshot(html_file=html_file.filename, save_as=f'{curr_time}.png')
    os.remove(html_file.filename)
    await ctx.send("ok", file=discord.File(f'{output_path}/{curr_time}.png'))
    

bot_id_list = [1186326404267266059, 839794863591260182, 944245571714170930, 1396935480284680334, 1414634216292876308, 1529839995639173320]

@client.event
async def on_message(message: discord.Message):
    await client.process_commands(message)
    if message.author.id not in bot_id_list and message.author.id != client.application_id:
        if "ugli" in message.content.lower():
            await message.channel.send("hi i ugli")

@client.event
async def on_command_error(ctx, error):
    channel_id = 1131914463277240361
    channel = client.get_channel(channel_id)
    await channel.send(error)
    await channel.send(error.__traceback__)

client.run(token)
