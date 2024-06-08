from django.shortcuts import render

# Create your views here.
def login_views(request):
    return render(request,'accounts/login.html')
def singup_views(request):
    return render(request,'accounts/singup.html')
#def loguot_views(request):
#    return 