from django.shortcuts import render
from .models import Conference,Journal
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


############################################################################################################################

def Options(request):
    return render(request,'options.html')

##########################################################################################################################

class conferencelist(ListView):
    model=Conference
    context_object_name='conference' 
    template_name='conferencelist.html'
     
    
def conference_details(request):
    conferences = Conference.objects.all()
    return render(request, 'conferencedetail.html', {'conferences': conferences})


class conferencecreate(CreateView):      
    model=Conference
    fields="__all__"
    template_name='conferencecreate.html'
    success_url=reverse_lazy('conference')      

##########################################################################################################################
    
class journallist(ListView):
    model=Journal
    context_object_name='journal' 
    template_name='journallist.html'
     
def journal_details(request):
    journals = Journal.objects.all()
    return render(request, 'journaldetail.html', {'journals':journals})

class journalcreate(CreateView):      
    model=Journal
    fields="__all__"
    template_name='journalcreate.html'
    success_url=reverse_lazy('journal')      

##########################################################################################################################