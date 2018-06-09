from django import forms

class HomeForm(forms.Form):
    your_text = forms.CharField(label='Text To Process', max_length=2000, widget = forms.Textarea)


class CountForm(forms.Form):
    your_text = forms.CharField(label='Text To Process', max_length=2000, widget = forms.Textarea)