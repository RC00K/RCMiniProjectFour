from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.utils import timezone
from .models import Choice, Poll, Vote, Post
# Form Imports
from .forms import NewUserForm, ReviewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class ReviewView(generic.View):
    def get(self, request):
        polls = Poll.objects.all()
        return render(request, template_name='portfolio/review.html', context={"polls": polls, })


class PollView(generic.View):
    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(request, template_name='portfolio/detail.html', context={"poll": poll, })

    def post(self, request, poll_id):
        requestData = request.POST

        choice_id = requestData.get('choice_id')

        try:
            poll = Poll.objects.get(id=poll_id)
            choice = Choice.objects.get(id=choice_id)
            Vote.objects.create(
                poll=poll,
                choice=choice,
            )

            poll_results = []
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question rating form
            return render(request, 'portfolio/detail.html',
                          context={"error_message": "No Choice Selected - Try Again", })
        else:
            for choice in poll.choices.all():
                voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
                poll_results.append([choice.name, voteCount])

            return render(request, template_name='portfolio/detail.html',
                          context={"poll": poll, "success_message": "Voted Successfully",
                                   "poll_results": poll_results, })


# Registration request
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("review")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render(request=request, template_name="auth/register.html", context={"register_form": form})


# Login request
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("review")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="auth/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("review")


def HomeView(request):
    return render(request, "portfolio/home.html")


def AboutView(request):
    return render(request, "portfolio/about.html")


def SkillsView(request):
    return render(request, "portfolio/skills.html")


def ServicesView(request):
    return render(request, "portfolio/services.html")


def ContactView(request):
    return render(request, "portfolio/contact.html")


class PostListView(ListView):
    model = Post
    template_name = "portfolio/review.html"
    context_object_name = 'posts'
    ordering = ['date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body"]
    template_name = "portfolio/create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = "portfolio/update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "portfolio/delete.html"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
