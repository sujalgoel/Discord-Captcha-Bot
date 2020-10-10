<h1 align="center">Discord captcha BOT 🤖</h1>
A Discord bot that requires users to answer a captcha to enter in your server. This bot is brand new and in beta so please do not expect it to be perfect.

# Requirements
### discord.py and captcha

Tested with Python 3.7 on Windows 10...

# Features
- Sets a user to a limited role upon joining the server.
- DM's the user a captcha to solve to have the role removed.
- Allows the user to request a new captcha if the current one is too hard.

# Setup Instructions
- Install the required modules!
- Create a new application at https://discordapp.com/developers/applications
- Turn it into a bot. Copy the token and put it on line 65 of `DiscordCaptcha.py`
- On the developer portal, Select `OAuth2`
- Select the `bot` checkmark and then `Manage Roles`
- Copy the generated link and paste it in your browser. Select the server to add it to.
- Go to your server settings and find roles. Move the bot role above all user roles.
- Create your limited role and ensure that it is below the bot's role.
- Now, Disable the read message permission for that role from the channel for which you want that role should not read the content!
- Copy the limited role's ID and put it on line 11 of `DiscordCaptcha.py`
- Copy your server's ID and put it on line 13 of `DiscordCaptcha.py`
- Run `DiscordCaptcha.py`
