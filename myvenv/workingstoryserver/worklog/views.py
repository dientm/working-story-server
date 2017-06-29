from django.shortcuts import render
from django.utils.datetime_safe import strftime
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
import random
from worklog.dto.BeaconConfiguration import BeaconConfiguration
from .models import WorkLog, LocalBeacon

from django.utils.timezone import activate
from workingstoryserver import settings
# activate(settings.TIME_ZONE)
# Create your views here.




@csrf_exempt
def working_action(request):
    great_sample = ['안녕하세요', 'Have a good day', '즐거운 하루 되세요', '고맙습니다']
    goodbye_sample = ['안녕히 가세요', '좀더앉아노세요 :)', 'Goodbye, see you tomorrow']
    if request.method == 'POST':
        r = {}
        body = json.loads(request.body.decode('utf-8'))
        username = body['username']
        location = body['location']
        report = body['report']
        action = body['action']
        user = User.objects.get(username=username)
        log = WorkLog(user=user, action=action, location=location,report= report)
        log.save(True)

        r['statusCode'] = 200
        if action == 1:
            r['message'] = random.choice(great_sample)
        elif action == 2:
            r['message'] = random.choice(goodbye_sample)
        return HttpResponse(json.dumps(r))



def get_beacon_configuration(request):
    if request.method == 'GET':
        r = {}
        beacons = LocalBeacon.objects.all()

        results = [ob.as_json() for ob in beacons]
        r['beacons'] = results
        return HttpResponse(json.dumps(r))


def get_activity(request):

    r = []
    last_ten = WorkLog.objects.all().order_by('-id')[:10]
    # son_string = json.dumps([ob.__dict__ for ob in last_ten])
    # last_ten_in_ascending_order = reversed(last_ten)
    for act in last_ten:
        r.append({'username': act.user.username,
                  'name': act.user.first_name,
                  'action': act.get_action_display(),
                  'action_on': act.action_on.strftime('%Y-%m-%d %H:%M:%S'),
                  'note': act.report})

    return HttpResponse(json.dumps(r))


