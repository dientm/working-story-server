from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers

from worklog.dto.BeaconConfiguration import BeaconConfiguration
from .models import WorkLog, LocalBeacon
# Create your views here.


@csrf_exempt
def finish_working(request):
    if request.method == 'POST':
        r = {}
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        location = body['location']
        report = body['report']
        user = User.objects.get(username=username)
        worklog = WorkLog()
        worklog.user = user
        worklog.action = 2
        worklog.location = location
        worklog.report = report
        worklog.save(True)

        r['statusCode'] = 200
        r['message'] = 'Goodbye,%s .See you tomorrow' % user.first_name

        print(json.dumps(r))
        return HttpResponse(json.dumps(r))


@csrf_exempt
def start_working(request):
    if request.method == 'POST':
        r = {}
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        location = body['location']
        report = body['report']
        user = User.objects.get(username=username)
        worklog = WorkLog()
        worklog.user = user
        worklog.action = 1
        worklog.location = location
        worklog.report = report
        worklog.save(True)

        r['statusCode'] = 200
        r['message'] = 'Goodbye,%s .See you tomorrow' % user.first_name

        print(json.dumps(r))
        return HttpResponse(json.dumps(r))


@csrf_exempt
def working_action(request):
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
            r['message'] = 'Have a good day'
        elif action == 2:
            r['message'] = 'Goodbye'
        return HttpResponse(json.dumps(r))



def get_beacon_configuration(request):
    if request.method == 'GET':
        r = {}
        beacons = LocalBeacon.objects.all()

        results = [ob.as_json() for ob in beacons]
        r['beacons'] = results
        return HttpResponse(json.dumps(r))

