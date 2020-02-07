from abc import ABC, abstractmethod

from .constants import *
import requests


class PostEntity(ABC):

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass


class User(PostEntity):

    def __init__(self, *,
                 username=None,
                 email=None,
                 password=None,
                 first_name=None,
                 last_name=None,
                 phone=None,
                 ):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.posts_count = 0
        self.likes_count = 0
        self.jwt = None

    def post(self):
        res = requests.post(url=REGISTER_URL, data=self.to_dict())
        self.jwt = res.json().get('token')

    def increment_posts_count(self):
        self.posts_count += 1

    def increment_likes_count(self):
        self.likes_count += 1

    def get_jwt(self):
        if self.jwt:
            return self.jwt
        raise ValueError("Invalid")

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password1": self.password,
            "password2": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
        }

    def __str__(self):
        return repr(self.to_dict())


class Post(PostEntity):

    def __init__(self, *, title, content, user: User):
        self.user = user
        self.content = content
        self.title = content
        self.id = None

    def post(self):
        headers = {'Authorization': f'JWT {self.user.get_jwt()}'}
        res = requests.post(url=POSTS_CREATE_URL,
                            data=self.to_dict(),
                            headers=headers)
        self.id = res.json().get('id')
        self.user.increment_posts_count()
