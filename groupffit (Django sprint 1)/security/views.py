from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required 

from .form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm


#def security(request):
   #return render(request, 'security/welcome.html', {'today': datetime.today()})

#@login_required(login_url='/admin')
#def authorised(request):
   #return render(request, 'security/authorised.html', {})




def login_user(request):
    if request.method =="POST":
       
        form =NewUserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
            username= cd['username'],
            password = cd['password'])

            if user is not None:
               login(requst, user)
               return HttpResponse('authentification was successfull')

            else:
              return HttpResponse('authentification failed, please try again')
    else:

        form = NewUserForm()
    return render(request=request, template_name='login.html',context= {'form':form})   

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name ="register.html", context={'register_form':form} )

