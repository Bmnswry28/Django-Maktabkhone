from django import forms
from website.models import contact
class Nameforms(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
    def clean_name(self):
        return "Anonymous"
    subject = forms.CharField(required=False)