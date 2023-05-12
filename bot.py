from discord.ext import commands
import os
import random
import string

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print(client.user, 'ACTIVATED')


@commands.is_owner()
@client.command()
async def clear(ctx, amount=5):
    if amount == 0:
        return
    elif amount <= 20:
        amount += 1
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send('Clear mac is 20.')


@client.command()
async def generate_password(ctx, l=8):
    if l >=8 and l <=32:
        await ctx.send(''.join(random.choice(string.digits + string.ascii_letters) for _ in range(l)))
    else:
        await ctx.send('Length field must be between 8 and 32.')


@client.command()
async def roll_dice(ctx, dice_size=6):
    if dice_size >= 2 and dice_size <= 100:
        await ctx.send(random.randint(1, dice_size))
    else:
        await ctx.send('Dice size max is 100 and min is 2.')


@client.command()
async def calc(ctx, *, calc):
    await ctx.send(str(eval(calc.replace(' ', ''))))  


client.run(os.getenv('TOKEN'))