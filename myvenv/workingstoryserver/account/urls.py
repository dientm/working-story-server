from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^login$', view=views._login, name="login"),
    url(r'^register', view=views.register, name="register"),
]
