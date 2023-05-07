from django import forms
from app.models import *
class topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']

class webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url']

class accessrecordform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields=['author','date']