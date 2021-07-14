from django.shortcuts import render
from  django.http import HttpResponse
from blog import models
# Create your views here.

def index(request):
    testModel = models.Test.objects.get(pk=1)
    return render(request, 'index.html', {'testModel':testModel})
