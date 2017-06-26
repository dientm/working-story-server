import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from account.dto.acount import Account


@csrf_exempt
def _login(request):
    if request.method == 'POST':
        r = {}
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        username = email.split('@')[0]
        password = body['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            r['statusCode'] = 200
            acc = Account(user)
            r['user'] = acc.toJSON()
            print(json.dumps(r))
            return HttpResponse(json.dumps(r))
        else:
            return HttpResponse({"statusCode": 200})
    pass

@csrf_exempt
def register(request):
    if request.method == 'POST':
        r = {}
        body = json.loads(request.body.decode('utf-8'))
        email = body['email']
        username = email.split('@')[0]
        password = body['password']
        name = body['name']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = name
        user.save();
        r['statusCode'] = 200
        return HttpResponse(json.dumps(r))