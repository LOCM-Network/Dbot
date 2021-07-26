import os
import sys
import yaml
import requests
import discord

class BotClient(discord.Client):

	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		cmd = message.content
		if message.author == self.user:
			return
		if cmd == ".ping":
			await channel.send("pong")
		if cmd == ".players":
			response = requests.get("https://api.mcsrvstat.us/bedrock/2/mc.locm.cf:19132")
			if (response.json()['online']):
				players = response.json()['players']
				await channel.send("LOCM Players: " + str(players["online"]) + "/" + str(players["max"]))
				return
			await channel.send("Server Offline")
class config:

	def __init__(self):
		with open(os.path.dirname(os.path.abspath(__file__)) + "/config.yaml", 'r') as stream:
			try:
				yml = yaml.safe_load(stream)
				if yml["token"] == '':
					print("Token missing")
					sys.exit()
			except yaml.YAMLError as exc:
				print(exc)
		self.config = yml

	def get_token(self):
		return self.config["token"]

	def get_admins(self):
		return self.config["admins"]

client = BotClient()
config = config()
client.run(config.get_token())