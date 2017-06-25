from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^finishworking', view=views.finish_working, name="finishworking"),
    url(r'^get_beacon_configuration', view=views.get_beacon_configuration, name='get_beacon_configuration'),
]
