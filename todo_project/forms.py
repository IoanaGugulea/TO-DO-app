from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task  # Import your Task model
from django.forms.widgets import DateInput

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    due_date = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  # Format: YYYY-MM-DD
    )