import discord,asyncio,youtube_dl
from discord.ext import commands
import os



def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['$'] #Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot=commands.Bot(command_prefix=get_prefix,description='bigthm based!', help_command=None)




exts=['music'] #Add your Cog extensions here


@bot.event
async def on_ready():
    song_name='master jonah'  #Status name
    activity_type=discord.ActivityType.listening #Status type
    await bot.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(bot.user.name)






for i in exts:
    bot.load_extension(i)


bot.run(os.environ['TOKEN'])
