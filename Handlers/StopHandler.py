from discord.ext.commands import Context
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerResponse import HandlerResponse
from Music.BkdBot import BkdBot
from Parallelism.AbstractProcessManager import AbstractPlayersManager
from Parallelism.Commands import VCommands, VCommandsType
from typing import Union
from discord import Interaction


class StopHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: BkdBot) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if playersManager.verifyIfPlayerExists(self.guild):
            command = VCommands(VCommandsType.STOP, None)
            await playersManager.sendCommandToPlayer(command, self.guild, self.ctx)
            embed = self.embeds.STOPPING_PLAYER()
            return HandlerResponse(self.ctx, embed)
        else:
            embed = self.embeds.NOT_PLAYING()
            return HandlerResponse(self.ctx, embed)
