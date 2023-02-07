from django import forms
class contact_form(forms.Form):
    value = forms.CharField(max_length = 100)