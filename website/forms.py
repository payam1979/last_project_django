from django import forms
from website.models import contact, NewsLetter
from captcha.fields import CaptchaField
#

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
    
class contactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'
       # exclude = ['name']
        
        
        
        
        
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'