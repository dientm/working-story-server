import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.dto.acount import Account
from account.forms import AvatarUploadForm
from account.models import AvatarModel
DEFAULT_AVATAR  = 'pic_folder/default_avatar.png'

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
        a = AvatarModel()
        a.user = user
        a.avatar = DEFAULT_AVATAR
        a.save();
        r['statusCode'] = 200
        return HttpResponse(json.dumps(r))


@csrf_exempt
def upload_avatar(request, template="account/avatar_upload.html"):
    if request.method == 'POST':
        form = AvatarUploadForm(request)
        if form.is_valid():
            m = AvatarModel.objects.get(user=User.objects.get(username=request.POST['username']))
            m.model_pic = form.cleaned_data['image']

            m.save()
        return HttpResponse('image upload success')
    else:
        return render(request, template)
    return HttpResponseForbidden('allowed only via POST')


def get_avatar(request, username):
    print(username)

    try:
        avatar = AvatarModel.objects.get(user=User.objects.get(username=username))
        image_data = open(avatar.avatar.path, "rb").read()
    except:
        image_data = open(DEFAULT_AVATAR, 'rb').read()
    return HttpResponse(image_data)
    # return HttpResponse(avatar.avatar)


