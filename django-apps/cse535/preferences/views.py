from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext

from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render

from .models import preferences
from authen.models import Appuser

class PreferencesView(APIView):
    def post(self, request):
        request.post.get("userid", "")
        request.post.get("topic1", "")
        request.post.get("topic2", "")
        request.post.get("topic3", "")
        request.post.get("topic4", "")
        request.post.get("topic5", "")

        models.preferences(userid="12324",topic1=5,topic2=3,topic3=2,topic4=4,topic5=1).save()

        return HttpResponse("Hello, world. You're at the polls index.")

class pref_save(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        prefobj = preferences()
        userid = request.data.get('userid')
        userobj = Appuser.objects.filter(id=userid)
        if len(userobj) == 1:
            prefobj.userid = userobj[0]
            prefobj.topic1 = request.data.get('topic1')
            prefobj.topic2 = request.data.get('topic2')
            prefobj.topic3 = request.data.get('topic3')
            prefobj.topic4 = request.data.get('topic4')
            # prefobj.topic5 = request.data.get('topic5')
            try:
                prefobj.save()
            except:
                return Response({'status':'error'})
            return Response({'status':'successfull'})
        else:
            return Response({'status':'Invalid Request'})
