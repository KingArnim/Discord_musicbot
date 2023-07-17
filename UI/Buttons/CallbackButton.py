from typing import Awaitable
from Config.Emojis import VEmojis
from discord import ButtonStyle, Interaction, Message, TextChannel
from discord.ui import Button, View
from Handlers.HandlerResponse import HandlerResponse
from Messages.MessagesCategory import MessagesCategory
from Messages.MessagesManager import MessagesManager
from Music.BkdBot import BkdBot
import discord

class CallbackButton(Button):
    """When clicked execute a callback passing the args and kwargs"""

    def __init__(self, bot: BkdBot, cb: Awaitable, emoji: VEmojis, text_channel: TextChannel, guild_id: int, category: MessagesCategory, label=None, *args, **kwargs):
        super().__init__(label=label, style=ButtonStyle.secondary, emoji=emoji)
        self.text_channel = text_channel
        self.guild_id = guild_id
        self.category = category
        self.messages_manager = MessagesManager()
        self.bot = bot
        self.args = args
        self.kwargs = kwargs
        self.callback = cb
        self.view: View = None

    async def callback(self, interaction: Interaction) -> None:
        """Callback when the button is clicked"""
        # Return to Discord that this command is being processed
        await interaction.response.defer()

        response: HandlerResponse = await self.callback(*self.args, **self.kwargs)

        message = None
        if response and response.view is not None:
            message: Message = await self.text_channel.send(embed=response.embed, view=response.view)
            response.view.set_message(message)
        elif response.embed:
            message: Message = await self.text_channel.send(embed=response.embed)

        # Clear the last sent message in this category and add the new one
        if message:
            await self.messages_manager.addMessageAndClearPrevious(self.guild_id, self.category, message, response.view)

    def set_view(self, view: View):
        self.view = view

    def get_view(self) -> View:
        return self.view
        
        
class ThreadPlayerManager:
    def __init__(self):
        self.__playersThreads = {}

    def __deleteThread(self, guild):
        try:
            playerInfo = self.__playersThreads[guild.id]
            # Rest of the code to delete the thread and cleanup
        except KeyError:
            # Handle the case when the guild ID is not found
            print(f"Guild ID {guild.id} not found in playersThreads dictionary.")



class MusicButtonView(View):
    def __init__(self, bot: BkdBot, current_song, text_channel):
        super().__init__()
        self.bot = bot
        self.current_song = current_song
        self.text_channel = text_channel

    def create_callback_button(self):
        return CallbackButton(
            self.bot,
            self.bot.vconfig.play_similar_songs,
            VEmojis.MUSIC,
            text_channel=self.text_channel,
            guild_id=self.text_channel.guild.id,
            category=None,  # Replace with the actual category
            label="Play Similar Songs",
            current_song=self.current_song
        )

    async def interaction_check(self, interaction: Interaction) -> bool:
        return interaction.user.id != self.bot.user.id

    @discord.ui.button(label="Play Similar Songs", style=discord.ButtonStyle.secondary)
    async def play_similar_songs_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        callback_button = self.create_callback_button()
        await callback_button.callback(interaction)
