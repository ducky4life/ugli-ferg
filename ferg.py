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
temp_folder = "temp"

token = os.getenv("FERG_TOKEN")
hti = Html2Image(
    output_path=output_path,
    custom_flags=['--virtual-time-budget=1000', '--hide-scrollbars', '--default-background-color=00000000'],
)

if not os.path.exists(output_path):
    os.makedirs(output_path)

if not os.path.exists(output_path + "/" + temp_folder):
    os.makedirs(output_path + "/" + temp_folder)

client = commands.Bot(
    command_prefix=[f"!{bot_prefix} "],
    intents=intents)

@client.event
async def on_ready():
    print('Roboduck is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ITS UGLI FERG!"))
    await client.tree.sync()
# endregion

def get_image_path(image_name: str):
    return (output_path + "/" + image_name)

async def search_images(query: str="None"):
    all_images = []
    images = []
    distinct_images = []
    query = query.strip("```").replace("\\", "/")
    for path, subdirs, files in os.walk(output_path):
        for name in files:
            if name not in distinct_images:
                distinct_images.append(name)
                path = os.path.join(path, name).replace("\\", "/")
                all_images.append(path)

    images = [image_path for image_path in all_images if query.lower() in image_path]
    return images

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
async def load_html(ctx, *, html: str, name: str=None):
    await ctx.defer()
    filename = name if name != None else str(int(time.time()))
    filename = filename + ".png"
    hti.screenshot(html_str=html, css_str="", save_as=filename)
    await ctx.send("ok", file=discord.File(get_image_path(filename)))

@client.hybrid_command()
async def load_html_url(ctx, url: str, name: str=None):
    await ctx.defer()
    filename = name if name else str(int(time.time()))
    filename = filename + ".png"
    hti.screenshot(url=url, save_as=filename)
    await ctx.send("ok", file=discord.File(get_image_path(filename)))

@client.hybrid_command()
async def load_html_file(ctx, html_file: discord.Attachment, name: str=None):
    await ctx.defer()
    await html_file.save()
    filename = name if name else str(int(time.time()))
    filename = filename + ".png"
    hti.screenshot(html_file=html_file.filename, save_as=filename)
    os.remove(html_file.filename)
    await ctx.send("ok", file=discord.File(get_image_path(filename)))

@client.hybrid_command()
async def get_image(ctx, *, name: str=None):
    await ctx.defer()
    filename = (await search_images(name))[0]
    await ctx.send("ok", file=discord.File(filename))

@client.hybrid_command()
async def get_all_named_images(ctx):
    await ctx.defer()
    image_files = []

    for path, subdirs, files in os.walk(output_path):
        for name in files:
            if temp_folder not in path:
                image_files.append(name)

    await ctx.send("\n".join(image_files))


@client.hybrid_command()
async def set_image_size(ctx, width: str, height: str):
    original_size = hti.size
    try:
        hti.size = (int(width), int(height))
        await ctx.send(f"ok set size from {original_size[0]}x{original_size[1]} to {width}x{height}")
    except Exception as e:
        await ctx.send(str(e))
    

bot_id_list = [1186326404267266059, 839794863591260182, 944245571714170930, 1396935480284680334, 1414634216292876308, 1529839995639173320]

@client.event
async def on_message(message: discord.Message):
    await client.process_commands(message)
    if message.author.id not in bot_id_list and message.author.id != client.application_id:
        if "ugli" in message.content.lower():
            await message.channel.send("hi i ✨ ugli ✨")
        if "醜青蛙" in message.content.lower():
            await message.channel.send(":(")

@client.event
async def on_command_error(ctx, error):
    channel_id = 1131914463277240361
    channel = client.get_channel(channel_id)
    await channel.send(error)
    await channel.send(error.__traceback__)

client.run(token)
