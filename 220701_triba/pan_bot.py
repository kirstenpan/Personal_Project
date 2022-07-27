from multiprocessing.dummy import Event
from pydoc import cli
import discord
from discord.ext import commands, tasks
import random
import datetime
import json
import pandas as pd
import os
os.chdir(os.path.dirname(__file__))

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#load done_authors.txt in done_authors, unless is '', then create an empty list
done_authors_ = open('done_authors.txt').read()
if done_authors_ == '':
    done_authors = list()
else:
    done_authors = [int(x) for x in done_authors_.split('\n')[:-1]]
active_conversations = dict()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching))
    print('now running', client)
    
@client.event
async def on_member_join(member):
    await client.wait_until_ready()
    guild = client.get_guild(914756125583343638) # server ID
    #channel = guild.get_channel(996143863116861510) # channel ID
    #await channel.send(f'Welcome to the server {member.mention}!') # Welcome the member on the server
    await member.send(f'Question 1')

@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')
 
@client.event
async def on_message(message):
    id = message.channel.id
    author = str(message.author)
    #when someone writes in the chat he is the message.author
    #however, when the bot sends him a private message he also activates another instance of function, becoming the message.author
    #the bot cannot send a message to himself, so whenever a message.author shows to have testing_bot in the name: AVOID RUNNING MORE CODE (else: ERR)
    if author.find('testing_bot') == -1: #if the one sending a message is a real user
        if id == 914756125583343638:
            #if the message is sent in the intro channel
            if message.author.id not in done_authors:
                await message.author.send('Question 1')
                done_authors.append(message.author.id)
                #reactivate the on_message function, because the bot is sending a message, and ultimately goes to else
        try:
            #Q&A starting
            if len(active_conversations[id]) == 0:
                #we have asked one question yet, the user just replied with a new message
                active_conversations[id].append(str(message.content))
                #ask another question
                await message.author.send('Question 2')
            elif len(active_conversations[id]) == 1:
                active_conversations[id].append(str(message.content))
                await message.author.send('Question 3')
            elif len(active_conversations[id]) == 2:
                active_conversations[id].append(str(message.content))
                #assign role based on previous data
                #then clean the conversation from the dic
                await assign_role(id)
        except:
            pass
        # print(active_conversations)
    else:
        #the bot is writing in a private dm
        if id not in list(active_conversations.keys()):
            active_conversations[id] = list()
     

async def assign_role(id):
    #add user to the new channel

    #aasign role based on the data
    print(active_conversations[id])
    print(done_authors)
    #remove conversation
    active_conversations.pop(id)
    with open('done_authors.txt', 'w') as file:
        for author_id in done_authors:
            file.write(str(author_id)+'\n')

client.run('OTE0NDQzOTYxMjk1MzMxMzg4.YaNITQ.RKHV62MNGUptbjkwbiIj8Vn_ZeY')