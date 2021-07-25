from discord.ext import commands
import os
import sys
import yaml

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

with open(os.path.dirname(os.path.abspath(__file__)) + "/config.yaml", 'r') as stream:
	try:
		yml = yaml.safe_load(stream)
		if yml['token'] == '':
			print('Token missing')
			sys.exit()
	except yaml.YAMLError as exc:
		print(exc)

bot.run(yml['token'])