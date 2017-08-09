from django import forms
from regform.models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'first_name', 'last_name','college','year'}
