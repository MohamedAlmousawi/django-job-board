from django import forms
from .models import *
class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields='__all__'
        exclude = ['job']
class jobForm(forms.ModelForm):
    model = Job
    fields = '__all__'