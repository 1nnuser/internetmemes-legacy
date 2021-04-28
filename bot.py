import os
import discord
from discord.ext import commands
from config import prefix, acces, token


client = discord.Client()
client = commands.AutoShardedBot(shard_count=10, command_prefix= prefix)
client.remove_command('help')


@client.command()
async def load(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.load_extension(f'cogs.{extension}') #загружает расширение
        await ctx.send(f'Loaded "{extension}"')
        return
    else:
        return

@client.command()
async def unload(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.unload_extension(f'cogs.{extension}') # выгружает расширение
        await ctx.send(f'Unloaded "{extension}"')
        return
    else:
        return


for filename in os.listdir('./cogs'): # загружает все файлы (* .py)
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') # загружает файл без ".py", например: cogs.ping

client.run(token)