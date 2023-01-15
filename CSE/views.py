from django.shortcuts import render
from .models import Conference,Journal
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegistrationForm

############################################################################################################################

def Options(request):
    return render(request,'options.html')

##########################################################################################################################
     
    
def conference_details(request):
    conferences = Conference.objects.all()
    return render(request, 'conferencedetail.html', {'conferences': conferences})


class conferencecreate(CreateView):      
    model=Conference
    fields="__all__"
    template_name='conferencecreate.html'
    success_url=reverse_lazy('conferences')      
  
##########################################################################################################################
    
     
def journal_details(request):
    journals = Journal.objects.all()
    return render(request, 'journaldetail.html', {'journals':journals})

class journalcreate(CreateView):      
    model=Journal
    fields="__all__"
    template_name='journalcreate.html'
    success_url=reverse_lazy('journals')      

##########################################################################################################################

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')                      # redirect user to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


#########################################################################################################################

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            message = "You have logged in successfully"
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('success_login', message=message)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



##########################################################################################################################

def success_login(request, message):
    return render(request, 'success_login.html', {'message': message})









