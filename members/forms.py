from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":'form-control'}))
    first_name = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=10,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":'form-control'}))
    first_name = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    bio = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','bio')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 =  forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','social_media_insta','social_media_github','social_media_pinterest')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe Yourself in few words'}),
            #'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'social_media_insta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
            'social_media_github': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
            'social_media_pinterest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),

    }