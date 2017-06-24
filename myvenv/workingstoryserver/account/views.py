from django.shortcuts import render
from django.core import serializers

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def _login(request):
    if request.method == 'POST':
        r = {}
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            r['statusCode'] = 200
            user_obj = serializers.serialize('json', [user, ])
            r['user'] = user_obj

            return HttpResponse(json.dumps(r))
        else:
            return HttpResponse({"statusCode": 200})
    pass

@csrf_exempt
def register(request):
    if request.method == 'POST':
        pass