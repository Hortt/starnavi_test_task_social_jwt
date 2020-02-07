from itertools import chain

from bot.factories import RandomUserFactory
from .parsers import IniParser


class RequestsService:

    CONFIG_PARSER = IniParser

    def __init__(self, config_path=None):
        self.config = self.CONFIG_PARSER(config_path).parse()
        self.users = []
        self.posts = []
        self.likes = []

    def _create_users(self):
        print(self.config)
        for _ in range(self.config['BOT_LIMITS']['number_of_users']):
            u = RandomUserFactory().create()
            self.users.append(u)

    def _create_posts(self):
        print(self.config)
        for user in self.users:
            for _ in range(self.config['BOT_LIMITS']['posts_per_user']):
                post = RandomUserFactory(user).create()
                self.posts.append(post)

    def _create_likes(self):
        print(self.config)
        for _ in range(self.config['BOT_LIMITS']['number_of_users']):
            like = RandomUserFactory(user, post).create()
            self.likes.append(like)

    def create_entities(self):
        self._create_users()
        self._create_posts()
        self._create_likes()

    def _post_entities(self):
        for entity in chain(self.users, self.posts, self.likes):
            entity.post()

    def execute(self):
        self._create_users()
        self._post_entities()

