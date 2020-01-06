
# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from authen.models import Appuser,Group
from django.http import HttpResponse

# Create your views here.
from . import models

class QuestionsView(APIView):
    def post(self, request):
        user = request.data.get('user')
        group = Group.objects.filter(subject1=user)
        if len(group) == 0:
            group = Group.objects.filter(subject2=user)
        groupobj = group[0]
        solution1 = request.data.get('solution1')
        solution2 = request.data.get('solution2')
        solution3 = request.data.get('solution3')
        solution4 = request.data.get('solution4')
        solution5 = request.data.get('solution5')
        solution6 = request.data.get('solution6')
        solution7 = request.data.get('solution7')
        solution8 = request.data.get('solution8')
        solution9 = request.data.get('solution9')
        solution10 = request.data.get('solution10')
        solution11 = request.data.get('solution11')
        solution12 = request.data.get('solution12')
        solution13 = request.data.get('solution13')
        solution14 = request.data.get('solution14')
        solution15 = request.data.get('solution15')
        solution16 = request.data.get('solution16')
        solution17 = request.data.get('solution17')
        solution18 = request.data.get('solution18')
        solution19 = request.data.get('solution19')
        solution20 = request.data.get('solution20')
        userobj = Appuser.objects.filter(id=user)[0]
        models.Questions(group=groupobj,solution1=solution1,solution2=solution2,solution3=solution3,solution4=solution4,solution5=solution5,solution6=solution6,solution7=solution7,solution8=solution8,solution9=solution9,solution10=solution10,solution11=solution11,solution12=solution12,solution13=solution13,solution14=solution14,solution15=solution15,solution16=solution16,solution17=solution17,solution18=solution18,solution19=solution19,solution20=solution20).save()
        return HttpResponse("You posted a group's solutions!")
