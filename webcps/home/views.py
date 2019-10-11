from django.shortcuts import render, get_object_or_404
from .models import This_status

# Create your views here.

def home(request):
    now_status = This_status.objects.filter(title = 'now')
    for now in now_status:
        this_status = This_status.objects.filter(id = now.content)
    
    return render(request, 'home.html',{"status": this_status})

def notify(request, id):
    now_status = get_object_or_404(This_status, pk=6)
    now_status.content = id
    now_status.save()
    for now in now_status:
                this_status = This_status.objects.filter(id = now.content)

    return render(request, 'home.html', {"status": this_status})

def notify2(request, id):
    now_status = get_object_or_404(This_status, pk=7)
    now_status.content = id
    now_status.save()
    for now in now_status:
        this_status = This_status.objects.filter(id = now.content)

    return render(request, 'home.html',{"status": this_status})

def myplant(request):
    now_status = This_status.objects.filter(title = 'now')
    now2_status = This_status.objects.filter(title ='now2')
    return render(request, 'myplant.html', {"status":now_status,"status2":now2_status})

