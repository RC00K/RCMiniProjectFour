from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


# Forms go here
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Form detail for review
class ReviewForm(forms.ModelForm):
    title = forms.CharField(required=True)
    body = forms.CharField(required=True)

    def save(self, commit=True):
        review = super(ReviewForm, self).save(commit=False)
        if commit:
            review.save()
        return review

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ("user", )
