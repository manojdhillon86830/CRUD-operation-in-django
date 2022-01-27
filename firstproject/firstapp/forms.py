from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
    author=forms.CharField(label='Author')