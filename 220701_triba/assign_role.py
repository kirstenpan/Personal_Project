import discord

#client = discord.client()

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if (message_id != 996827999838142508):
        return

    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild.id, client.guilds)

    if (payload.emoji.name ==''):
        role = discord.utils.get(guild.roles, name = '')

    if (role is not None): 
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
            await member.add_roles(role)
            print("changed role")
        else: 
            print("member not found")
    else: 
        print("role not found")

client.event
client.run('OTE0NDQzOTYxMjk1MzMxMzg4.YaNITQ.RKHV62MNGUptbjkwbiIj8Vn_ZeY')