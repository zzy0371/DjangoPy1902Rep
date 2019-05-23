from django import forms
from .models import Comment
class CommentForm(forms.Form):
    name = forms.CharField(required=True, label="输入名字",  widget=forms.TextInput(attrs={"id":"id_name"}) )
    email = forms.EmailField(required=True,label="输入邮箱", widget=forms.EmailInput(attrs={"id":"id_email"}))
    url = forms.URLField(label="输入个人主页", widget=forms.URLInput( attrs={"id":"id_url"}))
    comment = forms.CharField(required=True,label="输入评论",widget=forms.Textarea( attrs={"id":"id_comment"})    )