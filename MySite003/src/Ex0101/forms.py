from django import forms

class Pic_Form(forms.Form):
    Name_Pic = forms.CharField(max_length=50)
    Image    = forms.ImageField()
