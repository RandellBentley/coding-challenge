from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from linkApp.models import WebSite

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
    website = WebSite(link_title=request.POST['link_title'])
    website.save()
    return redirect('/')

def delete(request, id):
    website = WebSite.objects.get(id=id)
    website.delete()
    return redirect('/')

def landingLink(request, id):
    website = get_object_or_404(WebSite, pk=id)

def update(request, id):
    website = WebSite.objects.get(id=id)
    website.link_title = request.POST['link_title']
    website.clicks = request.POST['clicks']
    website.save()
    return redirect('/')
    #return redirect('linkApp/index.html')

def edit(request, id):
    websites = WebSite.objects.get(id=id)
    context = {'websites': websites}
    return render(request, 'linkApp/edit.html', context)
