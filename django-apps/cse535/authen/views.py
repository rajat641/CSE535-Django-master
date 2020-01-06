from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import views
from .models import Appuser, Group
from preferences.models import preferences
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
from authen.grouping import save_group


# Create your views here.


class login(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        # cty = request.data.get('password')
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        if user :
            data = model_to_dict(user.appuser)
            data['status'] = 'Valid'
            return Response(data)
        else:
            return Response({'status':'Invalid'})
        # return Response({"response":cty})


class signup(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        # cty = request.data.get('password')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name=None
        mobile = None
        if request.data.get('last_name')!=None:
            last_name = request.data.get('last_name')
        if request.data.get('mobile')!=None:
            mobile = request.data.get('mobile')

        authobj = User.objects.create_user(username=email,email=email,password=password)
        authobj.save()
        try:
            new_user = Appuser()
            new_user.first_name=first_name
            new_user.user=authobj
            new_user.last_name=last_name
            new_user.email=email
            new_user.mobile=mobile
            new_user.save()
        except:
            authobj.delete()
        data={}
        data['used_id']=new_user.id
        data['Status'] = 'User Saved'
        return Response(data)

### To generate similarity scores among users and make and store groups according to compatibility.
class group_save(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        i = 0
        res = save_group()
        for group in res:
            new_group = Group()
            new_group.id= group[0]
            new_group.subject1 = group[1]
            new_group.subject2 = group[2]
            new_group.compatibility = group[3]
            print('saved')
            new_group.save()
            # data['%d'%(i)] = 'saved'
        return Response(res)
