from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import loader
from linkApp.models import WebSite
from django.db import IntegrityError
from .models import WebSite
from rest_framework import viewsets
from .serializers import WebSiteSerializer


def index(request):
    return HttpResponse("<p>Welcome to the home page</p>")

def linkList(request):
    link_referral_list = WebSite.objects.order_by('clicks')
    template = loader.get_template('linkApp/index.html')
    context = {
        'link_referral_list': link_referral_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    try:
        website = WebSite(link_title=request.POST['link_title'])
        website.save()
    except IntegrityError as e:
        link_referral_list = WebSite.objects.order_by('-clicks')
        return render_to_response("linkApp/index.html", {"message": 'A site already exists with this name',
                                                            "link_referral_list": link_referral_list})

    else:
        return redirect('/')

def delete(request, id):
    website = WebSite.objects.get(id=id)
    website.delete()
    return redirect('/')

def landingLink(request, site_name):
    website = WebSite.objects.get(link_title=site_name)
    template = loader.get_template('linkApp/detail.html')
    website.clicks += 1
    website.save()
    context = {
        'website': website,
    }
    return HttpResponse(template.render(context, request))

def update(request, id):
    website = WebSite.objects.get(id=id)
    website.link_title = request.POST['link_title']
    website.clicks = request.POST['clicks']
    website.save()
    return redirect('/')

def edit(request, id):
    websites = WebSite.objects.get(id=id)
    context = {'websites': websites}
    return render(request, 'linkApp/edit.html', context)

class WebSiteViewSet(viewsets.ModelViewSet):
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer
