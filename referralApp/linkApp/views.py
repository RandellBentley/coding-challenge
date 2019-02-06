from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from linkApp.models import WebSite

def index(request):
    return HttpResponse("<p>Welcome to the home page</p>")

def linkList(request):
    link_referral_list = WebSite.objects.order_by('clicks')[:5]
    template = loader.get_template('linkApp/index.html')
    context = {
        'link_referral_list': link_referral_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    website = WebSite(link_title=request.POST['link_title'])
    website.save()
    return redirect('/')

def delete(request, id):
    website = WebSite.objects.get(id=id)
    website.delete()
    return redirect('/')
