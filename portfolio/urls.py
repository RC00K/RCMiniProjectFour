from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    # Reviews and Post Creation
    path('', views.ReviewView.as_view(), name='review'),
    path('create/', views.CreateView, name='create'),
    # Other Pages
    path('home/', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('skills/', views.SkillsView, name='skills'),
    path('services/', views.ServicesView, name='services'),
    path('contact/', views.ContactView, name='contact'),
    # Account Management
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # Rate Details
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/', views.ResultsView.as_view(), name='results'),
    path('<int:poll_id>/', views.PollView.as_view(), name='detail')
]
