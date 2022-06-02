from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Members
from flower.models import Flower
from django.forms import ModelForm
from flower.models import Photo

class FlowerForm(ModelForm):
    """
    title = forms.CharField(label="Title", widget = forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name':'Description', 'rows':5, 'cols':65}))
    slug = forms.CharField(label="Slug", widget = forms.TextInput(attrs={'class': 'form-control'}))
    """

    class Meta:
        model = Flower
        # fields = ['title', 'description', 'slug']
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-control'})
        }
        labels = {
            'title':'名稱',
            'description':'敘述',
            'slug':'代號',
            'category':'類別',
            'tags':'標籤'
        }

class MemberForm(forms.Form):
    username = forms.CharField(label="使用者名稱", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    
class NewMemberForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def save(self, commit=True):
        user = super(NewMemberForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
       