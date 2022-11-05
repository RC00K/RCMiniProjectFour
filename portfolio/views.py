
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.utils import timezone
from .models import Choice, Poll, Vote
# Form Imports
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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
            return render(request, 'portfolio/detail.html', context={"error_message": "No Choice Selected - Try Again", })
        else:
            for choice in poll.choices.all():
                voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
                poll_results.append([choice.name, voteCount])

            return render(request, template_name='portfolio/detail.html', context={"poll": poll, "success_message": "Voted Successfully", "poll_results": poll_results, })


# Registration request
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("portfolio:review")
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
                return redirect("portfolio:review")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="auth/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("portfolio:review")


#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'portfolio/detail.html'


#class ResultsView(generic.DetailView):
#    model = Question
#    template_name = 'portfolio/results.html'


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


def UpdateView(request):
    return render(request, "portfolio/update.html")


def CreateView(request):
    return render(request, "portfolio/create.html")


