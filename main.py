import discord
import random
import pandas as pd
client = discord.Client()

@client.event
async def on_ready():
    print(f'Current Robot：{client.user}')
    print("Running ...")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg[:2] == '撩我':
        await message.channel.send(message.author.mention)
        df = pd.read_csv('./content.csv')
        row = df.shape[0]
        index = random.randint(0, row-1)
        sentence = df.iloc[index]["Content"]
        await message.channel.send(sentence)
    elif msg[:2] == '新增':

        await message.channel.send(message.author.mention)
        await message.channel.send("已新增 : " + msg[3:])
        df = pd.read_csv('./content.csv')
        added = pd.DataFrame([msg[3:]], columns=["Content"])
        df = pd.concat([df, added], ignore_index=True)
        df.to_csv('./content.csv',index = False, encoding='utf-8-sig')
    elif msg == '屁眼派對':
        await message.channel.send(r'https://tenor.com/view/%E5%93%88%E5%93%88-partydog-gif-19725429')
client.run('')

# import discord
# import random
# import pandas as pd
# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'Current Robot：{client.user}')
#     print("Running ...")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     msg = message.content
#     if msg[:3] != '!u3':
#         return
#     if msg[4:] == '撩我':
#         await message.channel.send(message.author.mention)
#         df = pd.read_csv('./content.csv')
#         row = df.shape[0]
#         index = random.randint(0, row-1)
#         sentence = df.iloc[index]["Content"]
#         await message.channel.send(sentence)
#     elif msg[4:6] == '新增':

#         await message.channel.send(message.author.mention)
#         await message.channel.send("已新增 : " + msg[7:])
#         df = pd.read_csv('./content.csv')
#         added = pd.DataFrame([msg[6:]], columns=["Content"])
#         df = pd.concat([df, added], ignore_index=True)
#         df.to_csv('./content.csv',index = False, encoding='utf-8-sig')
#     elif msg[4:8] == '屁眼派對':
#         await message.channel.send(r'https://tenor.com/view/%E5%93%88%E5%93%88-partydog-gif-19725429')
# client.run('MTAwNjQyODU1MDk1OTczMDcyMA.Gfd9Fh.soJcng3QDnN0_kBrV3YsyIlhqouNoglV-OERuE')