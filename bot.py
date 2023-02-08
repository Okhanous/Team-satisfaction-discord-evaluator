# bot.py
import os
import random
from json_to_array import get_semaines, indic_categorie_personne , indic_categorie_mean
from prometheus_client import Summary
from quickchart import QuickChart
from PIL import Image
from discord.ext import commands
from dotenv import load_dotenv
import csv
import pandas as pd
import numpy as np
from datetime import datetime
import threading
import discord
import asyncio
import json

day_week_first_check = 4
day_week_second_check = 5
seconds_checks = 20
emoji_valide = "✅"

#semaine de commencement du registre du bot : 31 janvier
week_offset = 4


message_categorie = ["motivation", "Work load", "Work environment", "productivity"]
emojis = ["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

pic_discord_accounts = {'''Team-member1-Id''':"Team-member1", '''Team-member2-Id''':"Team-member2",
 '''Team-member3-Id''':"Team-member3", '''discord-moderator-Id''':"discord-moderator"}
pic_discord_accounts_debug = {"discord-moderator":'''discord-moderator-Id'''}
pic_bot_id = ''' Bot ID '''

messages_in_discord = []
message_validation = ""
channel = ""
poll_actif = False
validation_chef = True

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')
 

@bot.event
async def on_ready():
    global bot
    global channel

    await bot.wait_until_ready()
    channel = bot.get_channel(id='''EnterTheChannelId''')

@bot.command(name = 'Project Manager')
async def nine_nine(ctx):
    await ctx.send("Louis aka Michael Scott !!")

@bot.command(name = 'Project helper')
async def nine_nine(ctx):
    await ctx.send("Que du bangerrr")

@bot.command(name = 'Responsable-GIT')
async def nine_nine(ctx):
    await ctx.send("The one and only Apostolos")

@bot.command(name = 'Responsable-Network')
async def nine_nine(ctx):
    await ctx.send("mr.robot :')")

@bot.command(name = 'Responsable-Quality')
async def nine_nine(ctx):
    await ctx.send("Second poteau Yohaannnnn  ")

@bot.command(name = 'Responsable-Tech')
async def nine_nine(ctx):
    await ctx.send("hoooooyahhh ")

@bot.command(name = 'Responsable-Salsa')
async def nine_nine(ctx):
    message = ctx.send("not Javier Mascherano")
    await message


@bot.command(name = 'Erasmus-Exchange-Boy')
async def nine_nine(ctx):
    await ctx.send("Missing mdr")

@bot.command(name = 'poll_indicateurs')
async def poll_indicateurs(ctx):
    await bot.wait_until_ready()
    global channel
    
    await sendFirstMessage(channel)
    await poll(channel)
    

async def sendFirstMessage(channel):
    firstMessage = "@dev\nBonjour ! \n C'est le moment de noter tes performances de la semaine"
    firstEmojis = ["🎆","🎉","🔥"]

    message = await channel.send(firstMessage)
    for emoji in firstEmojis :
        await message.add_reaction(emoji)

async def poll(channel):
    counter = 0
    global poll_actif
    global messages_in_discord
    global message_validation
    global emoji_valide
    global emojis
    messagesText = ["1. Veuillez noter avec un chiffre entre 1 et 10 votre **motivation** au cours de cette semaine \n",
    "2. Veuillez noter avec un chiffre entre 1 et 10 **la charge de travail** que vous avez reçu au cours de cette semaine \n",
    "3. Veuillez noter avec un chiffre entre 1 et 10  **l'ambiance de l'équipe** au cours de cette semaine \n",
    "4. Veuillez noter avec un chiffre entre 1 et 10  **la productivité de l'équipe** au cours de cette semaine \n"]
    dernier_message_text = "Pour conclure le sondage, validez avec: ✅"

    messages_in_discord=[]
    for message in messagesText:
        message_in_discord = await channel.send(message)
        messages_in_discord.append(message_in_discord)
        for emoji in emojis :
            await message_in_discord.add_reaction(emoji)
            #Test obtenir les utilisateurs qui ont réagi à un certain message avec un emoji spécifique
    message_validation = await channel.send(dernier_message_text)
    await message_validation.add_reaction(emoji_valide)
    '''
    await motivation(ids[0])
    '''

    poll_actif = True
'''
async def motivation(id):
    cache_msg = discord.utils.get(bot.cached_messages, id=id)
    if (cache_msg.reactions[0].emoji=="0️⃣"):
        users=await cache_msg.reactions[0].users().flatten()
        print(users[0])
'''

@bot.command(name="channel_id")
async def channel_id(ctx, *args):
    global channel
    channel = ctx
    return

@bot.command(name="validation_chef")
async def validation_chef_change(ctx, *args):
    global validation_chef
    validation_chef = not(validation_chef)
    await ctx.send("Le chef doit valider :" + str(validation_chef))
    return

@bot.command(name= 'restore_poll')
async def restore_poll(ctx, *args):
    global messages_in_discord
    global message_validation
    global channel

    if(args[0]=="aide"):
        await channel.send("restore_poll id_msg1 id_msg2 id_msg3 id_msg4 id_msg_valid")
        return

    for i in range(4):
        msg = await channel.fetch_message(args[i])
        messages_in_discord.append(msg)
    
    message_validation = await channel.fetch_message(args[4])

    for msg in messages_in_discord:
        print(msg.id)
    print(message_validation.id)

    if(message_validation.reactions[0].count > 1):
        await remplir_fichier()
    return


@bot.event
async def on_reaction_add(reaction,user):
    global poll_actif
    global message_validation
    global channel
    global emoji_valide
    global validation_chef

    if(poll_actif):
        if(reaction.emoji == emoji_valide and reaction.message.id == message_validation.id and ((user.id == '''Project-manager-id''' and validation_chef) or not(validation_chef))):
            poll_actif = False
            await remplir_fichier()
    return

async def remplir_fichier():
    global messages_in_discord
    global message_categorie
    global emojis
    global channel
    global pic_bot_id
    global week_offset


    await channel.send("sondage clôturé, attendez validation du bot...")

    dict_remplir = {}

    with open('test.json') as json_file:
        dict_remplir = json.load(json_file)
    
    week_number = str(datetime.today().isocalendar()[1] - week_offset)

    dict_remplir[week_number] = {}


    for message, categorie in zip(messages_in_discord,message_categorie):

        message = await channel.fetch_message(message.id)
        for reac in message.reactions:
            contenu = False
            list_users = await reac.users().flatten()
            for user in list_users:
                if(user.id != pic_bot_id):
                    if(len(dict_remplir[week_number].values()) == 0):
                        dict_remplir[week_number][pic_discord_accounts.get(user.id)] = {}
                    else:
                        if(not(pic_discord_accounts.get(user.id) in dict_remplir[week_number].keys())):
                            print(dict_remplir[week_number].keys())
                            print(pic_discord_accounts.get(user.id))
                            dict_remplir[week_number][pic_discord_accounts.get(user.id)] = {}

                    dict_remplir[week_number][pic_discord_accounts.get(user.id)][categorie]= emojis.index(reac.emoji)
                    print(dict_remplir)

    f = open("test.json","w")

    json.dump(dict_remplir,f)
    f.close()
    await channel.send("validation : stockage des données finalisé")
    return


'''****************************************************************************Summary***************************************************************'''

@bot.command(name = 'summary')
async def chart(ctx, *args):
    categorie = args[-1]
    global pic_discord_accounts
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 2.0
    qc.config = {"type":"line"}
    qc.config["data"]= {}
    qc.config["data"]["labels"] = get_semaines()
    datasets = []
    colors = ["blue", "red", "yellow", "green","pink","black","orange","purple"]
    for personne in pic_discord_accounts.values():
        datasets.append({
            "label": personne,
            "data": indic_categorie_personne(categorie, personne),
            "fill":"false",
            "borderColor":colors[list(pic_discord_accounts.values()).index(personne)]
        })
    qc.config["data"]["datasets"] = datasets

    qc.to_file('data/'+categorie+'/'+categorie+'.png')
    await ctx.send(qc.get_short_url())

@bot.command(name = 'summarizeCharts')
async def chart(ctx):
    global pic_discord_accounts
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 2.0
    qc.config = {"type":"line"}
    qc.config["data"]= {}
    qc.config["data"]["labels"] = get_semaines()
    datasets = []
    colors = ["blue", "red", "yellow", "green"]
    for categorie in message_categorie:
        datasets.append({
            "label": categorie,
            "data": indic_categorie_mean(categorie, pic_discord_accounts.values()) ,
            "fill":"false",
            "borderColor":colors[message_categorie.index(categorie)]
        })
    qc.config["data"]["datasets"] = datasets

    qc.to_file('data/'+"summaryCharts"+'/'+"summaryCharts"+'.png')
    await ctx.send(qc.get_short_url())

print()

# à update
@bot.command(name = 'Aide', help = "Comment Utiliser cleyrop chart")
async def chart(ctx):
    await ctx.send("Pour chaque jour pour lequel un indicateur est respecté ajoute 1 \n exemple : Javi à été motivé lundi, mardi et vendredi sa note sera 3. \n En choisissant un chiffre entre 1 et 5 note dans l'ordre [ta motivation, ta ponctualité, ta prise d'intiative, ta participation et ton absenteism] pendant cette semaine par exemple !chartOmar 5 2 1 4 0 1.")
    await ctx.send("Tu indiqueras le numéro de la semaine à la fin")



bot.run(TOKEN)
