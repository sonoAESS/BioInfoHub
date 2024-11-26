from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta: 
        #planteamos modelo a utilizar
        model=Task
        fields=['title','description','important',]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placehold':'Write a title'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placehold':'Write a description'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }