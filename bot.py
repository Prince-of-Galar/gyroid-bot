
#   L L O I D   T H E   G Y R O I D

#   A discord bot created for Animal Crossing Max Island

#   by Ymir | Prince_of_Galar

#-------------------- SETUP --------------------#

import discord
import asyncio
import os
import re
from discord.utils import get
from discord.ext import commands
from random import seed
from random import random
from random import choice

#--------------- GLOBAL VARIABLES ---------------#

client = discord.Client()

#-------------------- ROLE DEFINITIONS BY ID --------------------#

rolesIndex = [
    
    #for Everyone -- Pronoun Roles
    682317087003115551, # [0]  any pronouns
    681943616788365547, # [1]  they/them pronouns
    681943575533060157, # [2]  she/her pronouns
    681943264378486820, # [3]  he/him pronouns
    
    #for Villager Representative 🥉 -- Bronze Level -- Standard Roles
    682341125217845254, # [4]  standard cranky
    681970912979189791, # [5]  standard peppy
    681970974719344726, # [6]  standard normal
    681970781994876928, # [7]  standard jock
    682346113247739955, # [8]  standard lazy
    682346995524173860, # [9]  standard smug
    682347003531100188, # [10] standard snooty
    682347049597009962, # [11] standard uchi
    
    #for Villager Leader 🥈 -- Silver Level -- Dark Roles
    682340943566864495, # [12] dark cranky
    682342304677363723, # [13] dark peppy
    682342610375016485, # [14] dark normal
    682345572258414600, # [15] dark jock
    681970797941620772, # [16] dark lazy
    681970860659310751, # [17] dark smug
    682347005879648295, # [18] dark snooty
    682347051081924617, # [19] dark uchi
    
    #for Villager of Honor 🥇 -- Gold Level -- Pastel Roles
    681943332590845972, # [20] pastel cranky
    682341764857987073, # [21] pastel peppy
    682342464446791684, # [22] pastel normal
    682343112156381240, # [23] pastel jock
    682345105163944030, # [24] pastel lazy
    682346962166874149, # [25] pastel smug
    681970879521226863, # [26] pastel snooty
    681970939327414474, # [27] pastel uchi
    
    #for New Members -- the Resident Role
    681918633529704659  # [28] resident
    
    ]

#-------------------- GREET + ROLE USERS ON JOIN --------------------#

@client.event
async def on_member_join(member):
    channel = client.get_channel(id = 681917060556783718)
    role = member.guild.get_role(role_id = rolesIndex[28])
    await channel.send('✨ A new resident has arrived! Please welcome {}'.format(member.mention) + '! ✨')
    await member.add_roles(role)
    
#-------------------- ADD REACTION EVENTS --------------------#

@client.event
async def on_raw_reaction_add(payload):
    guild = await client.fetch_guild(guild_id = payload.guild_id)
    member = await guild.fetch_member(member_id = payload.user_id)
    channel = client.get_channel(id = payload.channel_id)
    message = await channel.fetch_message(id = payload.message_id)
    role = None
    
    islandToursChannels = [690643769623838760, 690644677212241976, 691622702028423178, 692139714974842880]
    
    #Check for Island Tours channels, add pins
    if payload.channel_id in islandToursChannels and payload.emoji.name == "📌":
            await message.pin()
    
    #Check for Welcome channel, add roles
    if payload.channel_id == 681922284382191681:
        #for Everyone -- Pronoun Roles
        if payload.message_id == 686680851508887553:
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[0]) #any pronouns 
            elif payload.emoji.name == '🇧':
                role = guild.get_role(role_id = rolesIndex[1]) #they/them pronouns
            elif payload.emoji.name == '🇨':
                role = guild.get_role(role_id = rolesIndex[2]) #she/her pronouns
            elif payload.emoji.name == '🇩':
                role = guild.get_role(role_id = rolesIndex[3]) #he/him pronouns
            else:
                return
    
        #for Villager Representative 🥉 -- Bronze Level -- Standard Roles
        elif (payload.message_id == 686654695221100584) and get(member.roles, id = 686651557840027744): 
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[4])  #standard cranky
            elif payload.emoji.name == "🇧":
                role = guild.get_role(role_id = rolesIndex[5])  #standard peppy
            elif payload.emoji.name == "🇨":
                role = guild.get_role(role_id = rolesIndex[6])  #standard normal
            elif payload.emoji.name == "🇩":
                role = guild.get_role(role_id = rolesIndex[7])  #standard jock
            elif payload.emoji.name == "🇪":
                role = guild.get_role(role_id = rolesIndex[8])  #standard lazy
            elif payload.emoji.name == "🇫":
                role = guild.get_role(role_id = rolesIndex[9])  #standard smug
            elif payload.emoji.name == "🇬":
                role = guild.get_role(role_id = rolesIndex[10]) #standard snooty
            elif payload.emoji.name == "🇭":
                role = guild.get_role(role_id = rolesIndex[11]) #standard uchi
            else:
                return
            
        #for Villager Leader 🥈 -- Silver Level -- Dark Roles        
        elif (payload.message_id == 686655350484893777) and get(member.roles, id = 686651723280023645): 
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[12]) #dark cranky
            elif payload.emoji.name == "🇧":
                role = guild.get_role(role_id = rolesIndex[13]) #dark peppy
            elif payload.emoji.name == "🇨":
                role = guild.get_role(role_id = rolesIndex[14]) #dark normal
            elif payload.emoji.name == "🇩":
                role = guild.get_role(role_id = rolesIndex[15]) #dark jock
            elif payload.emoji.name == "🇪":
                role = guild.get_role(role_id = rolesIndex[16]) #dark lazy
            elif payload.emoji.name == "🇫":
                role = guild.get_role(role_id = rolesIndex[17]) #dark smug
            elif payload.emoji.name == "🇬":
                role = guild.get_role(role_id = rolesIndex[18]) #dark snooty
            elif payload.emoji.name == "🇭":
                role = guild.get_role(role_id = rolesIndex[19]) #dark uchi
            else:
                return
        
        #for Villager of Honor 🥇 -- Gold Level -- Pastel Roles
        elif (payload.message_id == 686655795244302347) and get(member.roles, id = 686651878838501376): 
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[20]) #pastel cranky
            elif payload.emoji.name == "🇧":
                role = guild.get_role(role_id = rolesIndex[21]) #pastel peppy
            elif payload.emoji.name == "🇨":
                role = guild.get_role(role_id = rolesIndex[22]) #pastel normal
            elif payload.emoji.name == "🇩":
                role = guild.get_role(role_id = rolesIndex[23]) #pastel jock
            elif payload.emoji.name == "🇪":
                role = guild.get_role(role_id = rolesIndex[24]) #pastel lazy
            elif payload.emoji.name == "🇫":
                role = guild.get_role(role_id = rolesIndex[25]) #pastel smug
            elif payload.emoji.name == "🇬":
                role = guild.get_role(role_id = rolesIndex[26]) #pastel snooty
            elif payload.emoji.name == "🇭":
                role = guild.get_role(role_id = rolesIndex[27]) #pastel uchi
            else:
                return 
        await member.add_roles(role)
    
#-------------------- REMOVE REACTION EVENTS --------------------#

@client.event
async def on_raw_reaction_remove(payload):
    guild = await client.fetch_guild(guild_id = payload.guild_id)
    member = await guild.fetch_member(member_id = payload.user_id)
    channel = client.get_channel(id = payload.channel_id)
    message = await channel.fetch_message(id = payload.message_id)
    role = None

    islandToursChannels = [690643769623838760, 690644677212241976, 691622702028423178, 692139714974842880]
    
    #Check for Island Tours channels, add pins
    if payload.channel_id in islandToursChannels and payload.emoji.name == "📌":
        await message.unpin()
    
    #Check for Welcome channel, remove roles
    if payload.channel_id == 681922284382191681:
        #for Everyone -- Pronoun Roles
        if payload.message_id == 686680851508887553:
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[0]) #any pronouns 
            elif payload.emoji.name == '🇧':
                role = guild.get_role(role_id = rolesIndex[1]) #they/them pronouns
            elif payload.emoji.name == '🇨':
                role = guild.get_role(role_id = rolesIndex[2]) #she/her pronouns
            elif payload.emoji.name == '🇩':
                role = guild.get_role(role_id = rolesIndex[3]) #he/him pronouns
            else:
                return
    
        #for Villager Representative 🥉 -- Bronze Level -- Standard Roles
        elif (payload.message_id == 686654695221100584) and get(member.roles, id = 686651557840027744): 
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[4])  #standard cranky
            elif payload.emoji.name == "🇧":
                role = guild.get_role(role_id = rolesIndex[5])  #standard peppy
            elif payload.emoji.name == "🇨":
                role = guild.get_role(role_id = rolesIndex[6])  #standard normal
            elif payload.emoji.name == "🇩":
                role = guild.get_role(role_id = rolesIndex[7])  #standard jock
            elif payload.emoji.name == "🇪":
                role = guild.get_role(role_id = rolesIndex[8])  #standard lazy
            elif payload.emoji.name == "🇫":
                role = guild.get_role(role_id = rolesIndex[9])  #standard smug
            elif payload.emoji.name == "🇬":
                role = guild.get_role(role_id = rolesIndex[10]) #standard snooty
            elif payload.emoji.name == "🇭":
                role = guild.get_role(role_id = rolesIndex[11]) #standard uchi
            else:
                return
            
        #for Villager Leader 🥈 -- Silver Level -- Dark Roles        
        elif (payload.message_id == 686655350484893777) and get(member.roles, id = 686651723280023645): 
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[12]) #dark cranky
            elif payload.emoji.name == "🇧":
                role = guild.get_role(role_id = rolesIndex[13]) #dark peppy
            elif payload.emoji.name == "🇨":
                role = guild.get_role(role_id = rolesIndex[14]) #dark normal
            elif payload.emoji.name == "🇩":
                role = guild.get_role(role_id = rolesIndex[15]) #dark jock
            elif payload.emoji.name == "🇪":
                role = guild.get_role(role_id = rolesIndex[16]) #dark lazy
            elif payload.emoji.name == "🇫":
                role = guild.get_role(role_id = rolesIndex[17]) #dark smug
            elif payload.emoji.name == "🇬":
                role = guild.get_role(role_id = rolesIndex[18]) #dark snooty
            elif payload.emoji.name == "🇭":
                role = guild.get_role(role_id = rolesIndex[19]) #dark uchi
            else:
                return
        
        #for Villager of Honor 🥇 -- Gold Level -- Pastel Roles
        elif (payload.message_id == 686655795244302347) and get(member.roles, id = 686651878838501376): 
            if payload.emoji.name == "🇦":
                role = guild.get_role(role_id = rolesIndex[20]) #pastel cranky
            elif payload.emoji.name == "🇧":
                role = guild.get_role(role_id = rolesIndex[21]) #pastel peppy
            elif payload.emoji.name == "🇨":
                role = guild.get_role(role_id = rolesIndex[22]) #pastel normal
            elif payload.emoji.name == "🇩":
                role = guild.get_role(role_id = rolesIndex[23]) #pastel jock
            elif payload.emoji.name == "🇪":
                role = guild.get_role(role_id = rolesIndex[24]) #pastel lazy
            elif payload.emoji.name == "🇫":
                role = guild.get_role(role_id = rolesIndex[25]) #pastel smug
            elif payload.emoji.name == "🇬":
                role = guild.get_role(role_id = rolesIndex[26]) #pastel snooty
            elif payload.emoji.name == "🇭":
                role = guild.get_role(role_id = rolesIndex[27]) #pastel uchi
            else:
                return 
        await member.remove_roles(role)

#-------------------- CHECK MESSAGES FOR NEGATIVITY AND HATESPEECH --------------------#  

#Open the badwords text file
with open('./data/badwords.txt','r') as file:
    badwordsFile = file.read().split('|')

#Open the hatewords text file
with open('./data/hatewords.txt','r') as file:
    hatewordsFile = file.read().split('|')

@client.event 
async def on_message(message):
    if message.channel.type != discord.ChannelType.private and message.author != client.user: # make sure message author is not the bot itself
        #FV definitions
        ft = 0
        ftUserList = message.guild.members
        
        #Badwords and hatewords filter definitions
        alertChannel = client.get_channel(686993684688011371) # define the "isabelles-desk" alert channel
        mutedQueue = client.get_channel(681976879871426733) # define the "muted-queue" restricted channel
        rulesChannel = client.get_channel(681923052669370388) # define the "principles" rules channel
        member = message.author
        modRole = message.guild.get_role(681917732123312188) # define the modRole as "Island Staff"
        mutedRole = message.guild.get_role(role_id = 681980308723073264)

        #Mod channels definitions
        modActionChannels = [681923559022788654, 681938549485994000, 681948931491364876, 693659563886510110, 686993684688011371, 694550205814800434]

        #Island Tour channels definitions
        islandToursChannels = [690643769623838760, 690644677212241976, 691622702028423178, 692139714974842880]
        splitMessage = message.content.split(' ')
        defaultName = '🌴-island-tours-🌴'
        defaultTopic = 'Type !tour-help for a guide on getting started!'

        #Creates and sends an alert if the message contains negative language
        for badwords in badwordsFile:
            if badwords in message.content.lower(): 
                alert = discord.Embed()
                alert.title = '*Negative Language Alert*'
                alert.add_field(name = 'User', value = message.author)
                alert.add_field(name = 'Message', value = message.content)
                alert.add_field(name = 'Link to Message', value = message.jump_url, inline = False)
                await alertChannel.send(embed = alert)
        
        #Creates and sends an alert if the message contains hateful language
        for hatewords in hatewordsFile:
            if hatewords in message.content.lower():
                alert = discord.Embed()
                alert.title = '⚠ ***Hateful Language Alert*** ⚠'
                alert.add_field(name = 'User', value = message.author)
                alert.add_field(name = 'Channel', value = message.channel.name)
                alert.add_field(name = 'Message', value = message.content)
                alert.add_field(name = 'Actions', value = 'The user has been muted for using hateful language.')
                await alertChannel.send(embed = alert)
                await message.delete() # deletes the user's message
                await member.add_roles(mutedRole) #sends the user to the muted-queue channel
                await mutedQueue.send('Greetings, {}!\n'.format(member.mention) + 'You are currently muted. Please take a moment to review our community {},'.format(rulesChannel.mention) + ' an {}'.format(modRole.mention) + ' member will be with you shortly.') 
        
        #Mod channel commands    
        if message.channel.id in modActionChannels:
            #Help function
            if splitMessage[0] == '!help':
                await message.channel.send('The current available commands are !mute, !kick, !ban, and !dm')
            
            #Mute function            
            elif splitMessage[0] == '!mute':
                member = await message.guild.fetch_member(member_id = splitMessage[1])
                await member.add_roles(mutedRole)
            
            #Kick function
            elif splitMessage[0] == '!kick':
                member = await message.guild.fetch_member(member_id = splitMessage[1])
                await member.kick
             
            #Ban function
            elif splitMessage[0] == '!ban':
                member = await message.guild.fetch_member(member_id = splitMessage[1])
                await member.ban

            #DM function    
            elif splitMessage[0] == '!dm':
                member = await message.guild.fetch_member(member_id = splitMessage[1])
                dmLogs =  client.get_channel(694550205814800434) # gets the post-office channel
                dmChannel = await member.create_dm()
                dmContent = '{}'.format(' '.join(splitMessage[2:]))
                
                dmSummary = discord.Embed()
                dmSummary.title = '📨 ***Direct Message Sent***  📨'
                dmSummary.add_field(name = 'Sender', value = message.author.mention)
                dmSummary.add_field(name = 'Recipient', value = member.mention)
                dmSummary.add_field(name = 'Message', value = dmContent)
                                
                await message.delete()
                await dmChannel.send(dmContent)
                await dmLogs.send(embed = dmSummary)
           
            #Add FV
            elif splitMessage[0] == '!addFV':
                member = await message.guild.fetch_member(member_id = splitMessage[1])
                
        
            #Emergency giveaway command, picks a random user on the server and prints username to alerts channel
            elif splitMessage[0] == '!giveaway':
                members = message.guild.members
                winner = choice(members)
            
                announcement = discord.Embed()
                announcement.add_field(name = '🎉 Winner! 🎉', value = winner)      
                await alertChannel.send(embed = announcement)
            
            #Print server member list
            elif splitMessage[0] == '!members':
                print(message.guild.members)
        
        #Island Tour channel commands
        elif message.channel.id in islandToursChannels:
        
            #Tour-help command
            if splitMessage[0] == '!tour-help':
                tourGuide = discord.Embed()
                tourGuide.title = '🏝️ ***Island Tours Guide*** 🏝️'
                tourGuide.add_field(name = '!name', value = '`!name channel-name`\nPlease note that channel names must be one long title seperated by hypens. Any other format will have unusual results!')
                tourGuide.add_field(name = '!topic', value = '`!topic Dodo code HERE1`\nWrite anything you like! This is a good place to put your Dodo code if you have one.')
                tourGuide.add_field(name = '!end', value = 'This command will set the channel name and topic back to their original format!')
                await message.channel.send(embed = tourGuide)
        
            #Channel name command
            elif splitMessage[0] == '!name':
                await message.channel.edit(name = splitMessage[1])
                await message.channel.send('The channel name has been changed!')
        
            #Channel topic command
            elif splitMessage[0] == '!topic':
                await message.channel.edit(topic = '{}'.format(' '.join(splitMessage[1:])))
                await message.channel.send('The channel topic has been set!')
        
            #End tour command
            elif splitMessage[0] == '!end':
                await message.channel.edit(name = defaultName)
                await message.channel.edit(topic = defaultTopic)
                await message.channel.send('Thank you for hosting! See you next time 🏝️')
   
    #Collect DM replies
    elif message.channel.type == discord.ChannelType.private and message.author != client.user:
        dmLogs =  client.get_channel(694550205814800434) # gets the post-office channel
        replySummary = discord.Embed()
        replySummary.title = '📩 ***Direct Message Recieved***  📩'
        replySummary.add_field(name = 'Sender', value = message.author.mention)
        replySummary.add_field(name = 'Message', value = message.content)
        await dmLogs.send(embed = replySummary)

#-------------------- RUN LLOID --------------------#

@client.event
async def on_ready():
    print('Lloid the Gyroid is ready to assist!')

#Runs the app
if __name__ == '__main__':
    client.run(os.environ.get('TOKEN'))