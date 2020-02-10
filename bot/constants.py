from django.conf import settings

API_BASE = settings.API_HOST

REGISTER_URL = API_BASE+'api/accounts/register/'
POSTS_CREATE_URL = API_BASE+'api/posts/'
POSTS_LIKE_TEMPLATE_URL = API_BASE+'api/posts/{}/like/'
LOGIN_URL = API_BASE + 'api/token/auth/'
