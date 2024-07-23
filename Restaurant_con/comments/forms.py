from django import forms
from.models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'İsminiz',
        }),required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Mailiniz',
        }),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
        'default':'comments/default.jpg'
    }),required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Mesajınız',
        
        }))
    class Meta:
        model = Comment
        fields = ['name','email','image','message']