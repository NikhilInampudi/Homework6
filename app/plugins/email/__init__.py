import logging
import sys
from app.commands import Command


class EmailCommand(Command):
    def execute(self):
        logging.info("Emailing you")
        print(f'Emailing you')