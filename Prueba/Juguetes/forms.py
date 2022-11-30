from django import forms
from Juguetes.models import Juguetes


class RegistroJuguete(forms.ModelForm):

    a = [('edad1','1-5'),('edad2','5-10'),('edad3','10-17'),('edad4','+18')]

    edad = forms.CharField(widget=forms.Select(choices=a))
    
    class Meta:
        model = Juguetes
        fields = '__all__'
        