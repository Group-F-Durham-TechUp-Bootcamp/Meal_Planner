from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatternsatterns 

#urlpatterns =[
#path('security', views.security),
    #path('authorised', views.authorised),
#]

  
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register' , views.register_request,  name="signup"),
    
]
urlpatterns += staticfiles_urlpatterns()  
    
