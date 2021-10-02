from django import forms
from . import models
class articelCreate(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','slug','body','image']
