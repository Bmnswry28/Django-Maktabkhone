from django.shortcuts import render
from website.forms import Nameforms
from django.contrib import messages
def index_view(request):
    return render(request, 'website\index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = Nameforms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'successfull')
        else:
            messages.add_message(request,messages.ERROR,'ERROR')
    form = Nameforms()
    return render(request, 'website/contact.html',{'form':form})
def coming_soon(request):
    return render(request, 'coming_soon.html')