from django import forms
from django.forms import ModelForm
from .models import Book

class DateInput(forms.DateInput):
    input_type = 'date'

class Book_input_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author', 'publish_date' )
        widgets = {
            'publish_date': DateInput(),
        }
