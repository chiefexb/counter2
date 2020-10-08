from django import forms
class Syst_standForm(forms.ModelForm):
    nexus_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Syst_stand

