import discord
from discord.ext import commands
import random 
from colorama import Fore, Style


client = commands.Bot(command_prefix = ".", case_insensitive = True)


@client.event
async def on_ready():
  print(Fore.CYAN + '''

 █▀▀█ █▀▀▀█ ▀▀█▀▀
 █▀▀▄ █░░▒█ ░▒█░░
 █▄▄█ █▄▄▄█ ░▒█░░''')
  
  print('Logado com: {0.user}' .format(client))
  print('Feito por yGuilherme0')
  print(Fore.MAGENTA +'Servidor de Suporte : https://discord.gg/tHQYT5Eu8T')
  
   





#resposa comum
@client.command()
async def ola(ctx):
  await ctx.send(f'oi {ctx.author} eu sou desenvolvido por yGuiherme')


#embed
@client.command()
async def enviarembed(ctx):
  embed = discord.Embed(
   title = 'Aula 1 Curso Bot Python',
   description = 'Eu estou ensinando a você fazer um bot em python',
   colour = discord.Colour.blue()
  )

  await ctx.send(embed = embed)
















#token

client.run("ODk2OTY2MjE3OTYzNzk4NTI5.YWOy4w.W7mjNEpX8lH46fyUWrpodpRw8SY")
