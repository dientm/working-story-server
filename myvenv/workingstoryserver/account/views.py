import json

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from account.dto.acount import Account
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
            acc = Account(user)
            # user_obj = serializers.serialize('json', [acc, ])
            r['user'] = acc.toJSON()
            print(json.dumps(r))
            return HttpResponse(json.dumps(r))
        else:
            return HttpResponse({"statusCode": 200})
    pass

@csrf_exempt
def register(request):
    if request.method == 'POST':
        pass