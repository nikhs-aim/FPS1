from django.urls import path
from .views import conference_details,conferencecreate,journal_details,journalcreate,Options
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('conferences/', conference_details, name='conferences'),
    path('conf-create/',conferencecreate.as_view(),name='conf-create'),
    path('journals/', journal_details, name='journals'),
    path('journal-create/',journalcreate.as_view(),name='journ-create'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('options',Options,name='options')
    
]




















# {% if request.user.is_authenticated %}
# <p>{{request.user}}</p>
# <a href="{% url 'logout' %}">Logout</a>
# {% else %}
# <a href="{% url 'login' %}">Login</a>
# {% endif %}
# <hr>










