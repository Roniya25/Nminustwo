from  django import  forms

class reg(forms.Form):
    nme = forms.CharField(max_length=20)
    add = forms.CharField(max_length=50)
    eml = forms.EmailField(max_length=20)
    usr = forms.CharField(max_length=15)
    psw = forms.CharField(max_length=8)
