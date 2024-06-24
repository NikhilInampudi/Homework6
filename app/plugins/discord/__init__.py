import logging
import sys
from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        logging.info("Sending info to discord")
        print(f'Sending info to discord')