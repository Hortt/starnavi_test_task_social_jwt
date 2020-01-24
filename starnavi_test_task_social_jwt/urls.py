from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


schema_view = get_swagger_view(title='Social API')

urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path('api/', include('accounts.urls')),
    url('api/api-token-auth/', obtain_jwt_token),
    url('api/api-token-refresh/', refresh_jwt_token),
    url('api/api-token-verify/', verify_jwt_token),
]


if settings.DEBUG:
    # import debug_toolbar

    urlpatterns = [
                      path('swagger/', schema_view),
                      # path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
