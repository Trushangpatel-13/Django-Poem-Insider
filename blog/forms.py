from django import forms
from .models import Post,CategoryList,Comment
choices = CategoryList.objects.all().values_list('name','name')
choices_list = []
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','id':'id_author','type':'hidden'}),

            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Describe your beautiful creation'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hey there Check my new Post'}),

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

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }