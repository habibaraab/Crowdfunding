# projects/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Donation, validate_egyptian_phone_number

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Email must be unique.')
    mobile_phone = forms.CharField(label="Mobile Phone", validators=[validate_egyptian_phone_number], required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile_phone')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_time', 'end_time', 'main_picture']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Launching an educational app for children'}),
            'details': forms.Textarea(attrs={'placeholder': 'Explain all the details of your project here...'}),
            'total_target': forms.NumberInput(attrs={'placeholder': 'e.g., 25000'}),
            'start_time': forms.DateInput(attrs={'type': 'date'}),
            'end_time': forms.DateInput(attrs={'type': 'date'}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter donation amount', 'class': 'donation-input'}),
        }
        labels = {
            'amount': 'Amount (in EGP)'
        }