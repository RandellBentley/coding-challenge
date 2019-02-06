from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from linkApp.models import WebSite

def index(request):
    return HttpResponse("<p>Welcome to the home page</p>")

def linkList(request):
    link_referral_list = WebSite.objects.order_by('clicks')[:5]
    template = loader.get_template('linkApp/home.html')
    context = {
        'link_referral_list': link_referral_list,
    }
    return HttpResponse(template.render(context, request))
