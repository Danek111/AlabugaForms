from django import forms

class Form(forms.Form):
    fname = forms.CharField(label='имя', max_length=100)
    lname = forms.CharField(label='фамилия', max_length=100)
    email = forms.CharField(label='почта', max_length=100)
    
    country = forms.CharField(label='страна', max_length=100)
    city = forms.CharField(label='город', max_length=100)
    street = forms.CharField(label='улица', max_length=100)
    num_of_home = forms.IntegerField(label='дом')
    num_of_flat = forms.IntegerField(label='квартира')
