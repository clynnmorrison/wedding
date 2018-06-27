from django.forms import ModelForm
from wedding.models import Rsvp, UserProfile
from django.forms.formsets import BaseFormSet
from django import forms
from django.utils.safestring import mark_safe

class HorizontalRadioWidget(forms.RadioSelect):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class RsvpForm(ModelForm):
    attending = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'class': 'inline'})
    )
    class Meta:
        model = Rsvp
        fields = ['name', 'attending']

class UserProfileForm(ModelForm):
   mailing_address = forms.CharField(widget=forms.Textarea)

   class Meta:
       model = UserProfile
       fields = ['mailing_address', 'comments']