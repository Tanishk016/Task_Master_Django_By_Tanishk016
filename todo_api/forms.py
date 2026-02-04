# todo_api/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    # This Meta class tells Django: "Build a form based on the Task model"
    class Meta:
        model = Task
        fields = ['title'] # We only want the user to edit the Title
        
        # Add CSS classes for styling (Bootstrap-ready)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'What is your next mission?'
            })
        }