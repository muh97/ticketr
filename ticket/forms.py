from django import forms
from .models import Ticket, Response, Company, Type
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('user_name', 'company', 'type', 'title', 'description', 'prior')

    widgets = {
        'user_name': forms.TextInput(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'company': forms.ChoiceField(),
        'prior': forms.ChoiceField(),
    }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('ticket', 'reply', 'comment')


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("{0} already existed".format(email))

        return email

class ResponseUpdateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('reply', 'comment')

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('description', 'prior')