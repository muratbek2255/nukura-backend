from django import forms


class AnketaForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    image = forms.ImageField(required=True)
    email = forms.EmailField(required=True)
    description = forms.CharField(required=True)