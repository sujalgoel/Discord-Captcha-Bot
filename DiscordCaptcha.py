import discord
import json
import CaptchaCreator
import os

class Client(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Set this to the limited role id you created.
        self.limitedRoleID = #ROLE_ID_HERE
        #Set this to your servers ID.
        self.serverID = #SERVER_ID_HERE

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        game = discord.Game("Captcha verification.")
        await client.change_presence(status=discord.Status.online, activity=game)

    def load_captchas(self):
        with open('captchas.json') as json_file:
            return json.load(json_file)

    def save_catchas(self, captchas):
        with open('captchas.json', 'w') as outfile:
            json.dump(captchas, outfile)

    async def on_member_join(self, member):
        server = client.get_guild(self.serverID)
        limitedRole = server.get_role(self.limitedRoleID)
        await member.add_roles(limitedRole)
        captcha_list = self.load_captchas()
        captchaValue = CaptchaCreator.create()
        captcha_list[member.id] = captchaValue
        self.save_catchas(captcha_list)
        file = "captcha_" + captchaValue + ".png"
        dmChannel = await member.create_dm()
        await dmChannel.send("**This server has enabled captcha verification.** **Please verify that you are a human by completing this challenge.**\n**Reply with `!v CAPTCHA_HERE`** to verify your account.\n**Reply with `!n`** **to get a new captcha, if this one is difficult!.**")
        await dmChannel.send(file=discord.File(file))
        os.system("rm " + file)

    async def on_message(self, message):
        server = client.get_guild(self.serverID)
        if message.channel.type == discord.ChannelType.private:
            captcha_list = self.load_captchas()
            if message.content.startswith("!v"):
                if captcha_list[str(message.author.id)] == message.content.split(" ")[1]:
                    await message.channel.send("You have been verified.")
                    captcha_list.pop(str(message.author.id))
                    self.save_catchas(captcha_list)
                    limitedRole = server.get_role(self.limitedRoleID)
                    await server.get_member(message.author.id).remove_roles(limitedRole)
                else:
                    await message.channel.send("Incorrect captcha.")
            elif message.content == "!n":
                captcha_list = self.load_captchas()
                captchaValue = CaptchaCreator.create()
                captcha_list[str(message.author.id)] = captchaValue
                self.save_catchas(captcha_list)
                file = "captcha_" + captchaValue + ".png"
                await message.channel.send(file=discord.File(file))
                os.system("rm " + file)

client = Client()
client.run('BOT_TOKEN_HERE')