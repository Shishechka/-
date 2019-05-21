# Create your views here.
#coding:utf-8
from django.http import HttpResponse
def home(request):
 return HttpResponse(u'Hello world!', mimetype="text/plain")
