from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    '''
    Each field type has a default widget that determines 
    how the field is rendered in HTML.
    Field validation also depends on the field type. 41d3be
    '''
    #  default is rendered as an <input type="text"> HTML element.
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    # widget attribute overrides default widget type
    # required is optional
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm): #page52
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
