from django.urls import path, re_path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    # Reviews and Post Creation
    path('', PostListView.as_view(), name='review'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
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
    path('<int:poll_id>/', views.PollView.as_view(), name='detail')
]
