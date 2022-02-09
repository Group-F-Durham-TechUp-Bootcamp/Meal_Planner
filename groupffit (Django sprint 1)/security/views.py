from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required 

def security(request):
    return render(request, 'security/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorised(request):
    return render(request, 'security/authorised.html', {})