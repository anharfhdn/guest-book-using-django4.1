from django import forms
from tamu.models import Tamu

class FormTamu(forms.ModelForm):
    
    class Meta:
        model = Tamu
        fields = "__all__"