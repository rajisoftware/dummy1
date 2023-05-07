from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic_web_access(request):
    tfo=topicform()
    wfo=webpageform()
    afo=accessrecordform()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=topicform(request.POST)
        wfd=webpageform(request.POST)
        afd=accessrecordform(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
           ustfo=tfd.save(commit=False)
           ustfo.save()
           uswfo=wfd.save(commit=False)
           uswfo.topic_name=ustfo
           uswfo.save()
           usafo=afd.save(commit=False)
           usafo.name=uswfo
           usafo.save()
           return HttpResponse('registrations is done successfully')
        else:
            return HttpResponse('not valid')
    return render(request,'insert_topic_web_access.html',d)
