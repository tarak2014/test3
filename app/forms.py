from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['notes','title']
        lables = {
            'notes': 'Note',
            'title' : 'Title',
            }