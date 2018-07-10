from django.forms import ModelForm
from wedding.models import Rsvp, UserProfile
from django.forms.formsets import BaseFormSet
from django import forms
from django.utils.safestring import mark_safe

class RsvpForm(ModelForm):
    attending = forms.ChoiceField(
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'class': 'inline'})
    )
    class Meta:
        model = Rsvp
        fields = ['name', 'attending', 'vegetarian_meal']

class UserProfileForm(ModelForm):
    mailing_address = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 30, 'data-parsley-errors-container': "#error_container",
               'data-parsley-error-message': "Mailing address is required"}, ), required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}), required=False)
    class Meta:
        model = UserProfile
        fields = ['mailing_address', 'comments']