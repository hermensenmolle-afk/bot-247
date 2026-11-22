import discord, os

TOKEN = os.environ.get("TOKEN")
VOICE_ID = int(os.environ.get("VOICE_ID"))

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot online!")
    channel = bot.get_channel(VOICE_ID)
    if channel:
        await channel.connect()

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == bot.user.id and after.channel is None:
        channel = bot.get_channel(VOICE_ID)
        if channel:
            await channel.connect()

bot.run(TOKEN)
