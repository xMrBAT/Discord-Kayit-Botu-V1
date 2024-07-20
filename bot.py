import discord
from discord.ext import commands
import json
import os

# Config dosyasını yükle
with open('config.json') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Kayıt sayıları için bir veri yapısı
if os.path.exists('register_counts.json'):
    with open('register_counts.json') as counts_file:
        register_counts = json.load(counts_file)
else:
    register_counts = {}

def process_message(message, member, inviter=None):
    message = message.replace('%user%', member.mention)
    message = message.replace('%server%', member.guild.name)
    message = message.replace('%member%', str(member.guild.member_count))
    
    if inviter:
        message = message.replace('%inviter%', inviter.mention)
    else:
        message = message.replace('%inviter%', 'Bilinmiyor')
    
    return message

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı.')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=int(config['role_on_join_id']))
    await member.add_roles(role)
    
    welcome_channel = bot.get_channel(int(config['welcome_channel_id']))
    welcome_message = process_message(config['welcome_message'], member)
    
    await welcome_channel.send(welcome_message)

@bot.command(name='k')
async def register(ctx, member: discord.Member, name: str, age: int):
    registered_role = discord.utils.get(ctx.guild.roles, id=int(config['registered_role_id']))
    role_on_join = discord.utils.get(ctx.guild.roles, id=int(config['role_on_join_id']))
    
    await member.edit(nick=f"{name} | {age}")
    await member.add_roles(registered_role)
    await member.remove_roles(role_on_join)
    
    # Kayıt sayısını güncelle
    if str(ctx.author.id) not in register_counts:
        register_counts[str(ctx.author.id)] = {'today': 0, 'week': 0, 'month': 0, 'total': 0}
    
    register_counts[str(ctx.author.id)]['today'] += 1
    register_counts[str(ctx.author.id)]['week'] += 1
    register_counts[str(ctx.author.id)]['month'] += 1
    register_counts[str(ctx.author.id)]['total'] += 1
    
    with open('register_counts.json', 'w') as counts_file:
        json.dump(register_counts, counts_file)
    
    log_channel = bot.get_channel(int(config['log_channel_id']))
    
    log_message = (f"{ctx.author.mention} {member.mention} kişisini kayıt etti. "
                   f"Bugün: {register_counts[str(ctx.author.id)]['today']}, "
                   f"Bu hafta: {register_counts[str(ctx.author.id)]['week']}, "
                   f"Bu ay: {register_counts[str(ctx.author.id)]['month']}, "
                   f"Toplam: {register_counts[str(ctx.author.id)]['total']}")
    
    await log_channel.send(log_message)

bot.run(config['token'])