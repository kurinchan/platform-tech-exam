from django.forms import ModelForm
from .models import *

class BlogForm(ModelForm):
    class Meta: #attach additional information
        model = Blog
        fields = ('blog_title', 'blog_content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blog_title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter title'})
        self.fields['blog_content'].widget.attrs.update({'class' : 'text-area form-control', 'placeholder' : 'Penny for your thoughts?', 'cols': '30', 'rows': '5'})

class CodeForm(ModelForm):
    class Meta: #attach additional information
        model = Code
        fields = ('code_title', 'code_content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code_title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'File Name'})
        self.fields['code_content'].widget.attrs.update({'class' : 'text-area form-control', 'placeholder' : 'Paste code here.', 'cols': '30', 'rows': '5'})
