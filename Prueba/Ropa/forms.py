from django import forms
from Ropa.models import Ropa

class RegistroRopa(forms.ModelForm):

    
    class Meta:

         model = Ropa
         fields = '__all__'