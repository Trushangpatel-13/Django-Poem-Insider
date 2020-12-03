from django import forms
from .models import Post,Category
choices = Category.objects.all().values_list('name','name')
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','categories','body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'categories':forms.Select(choices=choices,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Describe your beautiful creation'}),

        }
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control disabled','placeholder':'Tag'}),
            #'author': forms.Select(attrs={'class': 'disabled form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Describe your beautiful creation'}),

        }