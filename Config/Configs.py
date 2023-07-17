import discord
from decouple import config
from Config.Singleton import Singleton
from Config.Folder import Folder
import re
import os
import webbrowser
import urllib.parse

class VConfigs(Singleton):
    def __init__(self) -> None:
        self.CHANCE_SHOW_PROJECT = 50  # Example value, modify as needed
        if not super().created:
            # You can change this boolean to False if you want to prevent the Bot from auto disconnecting
            # Resolution for the issue: https://github.com/RafaelSolVargas/Bkd/issues/33
            self.CHANCE_SHOW_PROJECT = 50  # Example value, modify as needed
            self.SHOULD_AUTO_DISCONNECT_WHEN_ALONE = True
            # Recommended to be True, except in cases when your Bot is present in thousands servers, in that case
            # the delay to start a new Python process for the playback is too much, and to avoid that you set as False
            # This feature is for now in testing period, for a more stable version, keep this boolean = True
            self.SONG_PLAYBACK_IN_SEPARATE_PROCESS = False
            # Maximum of songs that will be downloaded at once, the higher this number is, the faster the songs will be all available
            # but the slower will be the others commands of the Bot during the downloading time, for example, the playback quality
            self.MAX_DOWNLOAD_SONGS_AT_A_TIME = 5

            self.BOT_PREFIX = '!'
            try:
                self.BOT_TOKEN = config('BOT_TOKEN')
                self.SPOTIFY_ID = config('SPOTIFY_ID')
                self.SPOTIFY_SECRET = config('SPOTIFY_SECRET')
                self.BOT_PREFIX = config('BOT_PREFIX')
            except:
                print('[ERROR] -> You must create an .env file with all required fields, see documentation for help')

            self.CLEANER_MESSAGES_QUANT = 5
            self.ACQUIRE_LOCK_TIMEOUT = 10
            self.QUEUE_VIEW_TIMEOUT = 120
            self.COMMANDS_FOLDER_NAME = 'DiscordCogs'
            self.COMMANDS_PATH = f'{Folder().rootFolder}{self.COMMANDS_FOLDER_NAME}'
            self.VC_TIMEOUT = 300

            self.MAX_PLAYLIST_LENGTH = 50
            self.MAX_PLAYLIST_FORCED_LENGTH = 5
            self.MAX_SONGS_IN_PAGE = 10
            self.MAX_PRELOAD_SONGS = 15
            self.MAX_SONGS_HISTORY = 15

            self.INVITE_MESSAGE = """To invite BKD_MUSIC to your own server, click [here]({}). 
            Or use this direct URL: {}"""

            self.MY_ERROR_BAD_COMMAND = 'This string serves to verify if some error was raised by myself on purpose'
            self.INVITE_URL = 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'

    def getPlayersManager(self):
        return self.__manager

    def setPlayersManager(self, newManager):
        self.__manager = newManager

    def get_current_song(self):
        # Example implementation to retrieve the currently playing song
        # Replace this with your logic to get the currently playing song
        # For the Discord bot, you can implement a method to fetch the currently playing song from the bot's playback or audio streaming functionality
        pass

    def play_similar_songs(self, current_song):
        # Encode the current song to be used in the YouTube search query
        encoded_song = urllib.parse.quote(current_song)

        # Construct the YouTube search URL
        search_url = f"https://www.youtube.com/results?search_query={encoded_song}&sp=EgIQAQ%253D%253D"

        # Open the YouTube search URL in the default web browser
        webbrowser.open(search_url)

        # Alternatively, if you have a music player library or an audio streaming API, you can play the songs directly
        # using the search query results from YouTube. Below is an example of playing the songs using the 'webbrowser' module.
        # Note: This example assumes you have a GUI environment and a web browser installed.

        # Wait for the user to select a song from the search results
        # In the case of a Discord bot, you can use a Discord message or reaction-based system to select the song

        # You can implement the necessary logic using discord.py library to handle interactions with Discord

        # Example:
        # - Send the search URL to the Discord channel
        # - Collect the user's response to choose a song
        # - Retrieve the selected song URL and open it in the default web browser using webbrowser.open

# Create an instance of the VConfigs class
vconfigs = VConfigs()

# Create an instance of the Discord bot client
bot = discord.Client()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    content = message.content.strip()

    # Check if the message starts with the bot prefix
    if content.startswith(vconfigs.BOT_PREFIX):
        command = content[len(vconfigs.BOT_PREFIX):].strip()
        if command.startswith('play_similar'):
            args = command.split(maxsplit=1)
            if len(args) > 1:
                current_song = args[1]
            else:
                current_song = vconfigs.get_current_song()
            vconfigs.play_similar_songs(current_song)
        else:
            await message.channel.send("Unknown command.")

