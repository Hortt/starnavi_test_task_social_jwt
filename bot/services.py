from bot.factories import RandomUserFactory
from .parsers import IniParser


class RequestsService:

    CONFIG_PARSER = IniParser

    def __init__(self, config_path=None):
        self.config = self.CONFIG_PARSER(config_path).parse()
        self.users = []

    def _create_users(self):
        print(self.config)
        for _ in range(self.config['BOT_LIMITS']['number_of_users']):
            u = RandomUserFactory().create()
            u.post()
            self.users.append(u)

    def _do_commands(self):
        self._create_users()
        # self._make_posts()
        # self._like_posts()

    def execute(self):
        self._create_users()

