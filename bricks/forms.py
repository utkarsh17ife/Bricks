from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=20)
    password = forms.CharField(min_length=5, max_length=20)


class SignupForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=15)
    password = forms.CharField(min_length=6, max_length=15)
    email = forms.CharField(min_length=6)
    first_name = forms.CharField(min_length=3, max_length=30)
    last_name = forms.CharField(min_length=1, max_length=30)
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=20)
    zip = forms.CharField(max_length=6)
    phone = forms.CharField(max_length=10)