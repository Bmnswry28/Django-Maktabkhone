from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login',views.login_views,name='login'),
    path('singup',views.singup_views,name='singup'),
    #path('loguot',views.loguot_views,name='loguot')
]