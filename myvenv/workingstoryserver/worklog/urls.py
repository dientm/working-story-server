from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^working-action', view=views.working_action, name='working_action'),
    url(r'^get-beacon-configuration', view=views.get_beacon_configuration, name='get_beacon_configuration'),
    url(r'^get-activity', view=views.get_activity, name='get_activity'),
]
