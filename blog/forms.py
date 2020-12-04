from django import forms
from .models import Post,CategoryList
choices = CategoryList.objects.all().values_list('name','name')
choices_list = []
for item in choices:
    choices_list.append(item)
print(choices_list)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
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