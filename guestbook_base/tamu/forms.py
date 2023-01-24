from django import forms
from tamu.models import Tamu

class FormTamu(forms.modelForm):
    
    class Meta:
        model = Tamu
        fields = "__all__"