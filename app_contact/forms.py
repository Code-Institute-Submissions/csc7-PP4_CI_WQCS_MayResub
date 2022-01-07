#https://docs.djangoproject.com/en/4.0/topics/forms/

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    surname = forms.CharField(label='Surname', max_length=50)
    email = forms.EmailField(label='E-Mail', max_length=100, required=False)
    text_content = forms.CharField(label='Description', max_length=2000)
