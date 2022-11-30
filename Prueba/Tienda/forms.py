from django import forms
from Tienda.models import Tienda


class RegistroTienda(forms.ModelForm):
    
    a = [('si','Si'),('no','No')]
    

    comprasOnline = forms.CharField(widget=forms.Select(choices=a))
    entregaDomicilio = forms.CharField(widget=forms.Select(choices=a))
    

    class Meta:
        
         model = Tienda
         fields = '__all__'
         
         