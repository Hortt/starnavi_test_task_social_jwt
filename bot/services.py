from .parsers import IniParser


class RequestsService:

    CONFIG_PARSER = IniParser

    def __init__(self, config_path=None):
        self.commands = []
        self.config = self.CONFIG_PARSER(config_path).parse()
        self.users = []

    def _create_users(self):


        self.users.append(user)
        yield user


    def _do_commands(self):
        for user in self._create_users():
            self._make_posts(user)
        self._like_posts()

    def execute(self):
        self._do_commands(self)
