import discord
import os
from discord.ext import commands, tasks
import keep_alive
from discord.utils import get
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!",
                              case_insensitive=True,
                              intents=intents)

@bot.event
async def on_message(message):
  if message.author.id == bot.user.id:
      return

  if message.author != message.author.bot:
      if not message.guild:
          if message.content in ['help','Help','HELP']:
              guild = bot.get_guild(900212436806828112)
              await message.channel.send('Enter feedback/query')
              a = await bot.wait_for('message',check = lambda message: message.author.id != bot.user.id ,timeout=120)
              await message.channel.send("Your message has been forwarded! Wait for a mod to answer your queries")
              category = discord.utils.get(guild.categories, id=918389826909249546)
              if not get(guild.channels, name=str(message.author.id)):
                  await guild.create_text_channel(message.author.id, overwrites=None, category=category, reason=None)
              channel = get(guild.channels, name=str(message.author.id))
              await channel.send(f"**{message.author.name}** : "+a.content + f" <@&900235804331343922><@&900234665753989120><@&900235408204529684>")
  await bot.process_commands(message)

@bot.command(pass_context=True)
async def cd(ctx):
    await ctx.channel.delete()

@bot.command(pass_context=True)
async def reply(ctx, *args):
    name = ctx.channel.name
    reply = " ".join(args)
    author = await bot.fetch_user(int(name))
    await author.send(f"**{ctx.author.name}:** "+reply)

   
keep_alive.keep_alive()
bot.run(os.getenv('TOKEN'))