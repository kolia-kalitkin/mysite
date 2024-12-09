from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Name'}))  # добавили в обработку формы поля name и email и к каждому полю мы добавили класс form-control, а также текстовую подсказку для пользователя в поле для ввода информации
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Email'}))
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Text'}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'E-Mail'}))
    to = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'To'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={"class": "form-control mb-1", 'placeholder': 'Comments'}))
    

class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Введите поисковый запрос...'}))