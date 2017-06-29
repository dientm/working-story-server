from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^login$', view=views._login, name="login"),
    url(r'^register', view=views.register, name="register"),
    url(r'^upload-avatar', view=views.upload_avatar, name="upload_avatar"),

    url(r'^avatar/(?P<username>\w+)/$', view=views.get_avatar, name='profile_view'),
]
