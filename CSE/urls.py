from django.urls import path
from .views import conference_details,conferencecreate,journal_details,journalcreate,Options
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [
    path('conferences/', conference_details, name='conferences'),
    path('conf-create/',conferencecreate.as_view(),name='conf-create'),
    path('journals/', journal_details, name='journals'),
    path('journ-create/',journalcreate.as_view(),name='journ-create'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('options',Options,name='options'),
     path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
   
]
    




























