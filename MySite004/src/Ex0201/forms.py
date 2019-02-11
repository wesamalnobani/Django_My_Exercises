from django import forms

class Users_Form(forms.Form):
    First_Name = forms.CharField() # Defualt True (required=True)
    Last_Name  = forms.CharField()
    Email      = forms.EmailField()
    Birth_Day  = forms.DateField()
