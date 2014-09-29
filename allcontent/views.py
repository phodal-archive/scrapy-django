from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from allcontent.models import Content
# Create your views here.

def home(request):
    object = Content.objects.all()[0]
    return render_to_response('home.html',{'result': object});