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
    if request.user.is_authenticated:
        conferences = Conference.objects.filter(fac_name=request.user)
    else:
        conferences = Conference.objects.all()
    return render(request, 'conferencedetail.html', {'conferences': conferences})


class conferencecreate(CreateView):
    model=Conference
    fields = ['conference_id', 'conference_name', 'conference_article', 'conference_doi', 'ugc_listed']
    template_name='conferencecreate.html'
    success_url=reverse_lazy('conferences')
   
    def form_valid(self, form):
        form.instance.fac_name = self.request.user
        return super().form_valid(form)    
  
##########################################################################################################################
    
     
def journal_details(request):
    if request.user.is_authenticated:
        journals = Journal.objects.filter(fac_name=request.user)
    else:
        journals = Journal.objects.all()
    return render(request, 'journaldetail.html', {'journals': journals})

class journalcreate(CreateView):
    model=Journal
    fields = ['journal_id', 'journal_name', 'journal_article', 'journal_doi', 'ugc_listed']
    template_name='journalcreate.html'
    success_url=reverse_lazy('journals')
   
    def form_valid(self, form):
        form.instance.fac_name = self.request.user
        return super().form_valid(form)
 

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
            return redirect('options')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



##########################################################################################################################











