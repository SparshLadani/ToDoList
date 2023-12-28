from django import forms

class newList(forms.Form):
    name = forms.CharField(max_length=200, label="Name of your list")
    confirm = forms.BooleanField(required=True)