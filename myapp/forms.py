from django import forms
    
class Contact_form(forms.Form):
    namef=forms.CharField()
    emailf=forms.EmailField()
    subjectf=forms.CharField()
    messagefen=forms.CharField()
