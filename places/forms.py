from django import forms

class PlaceForm(forms.Form):
    name_text = forms.CharField(label='Название места', max_length=50)
    comment_text = forms.CharField(label='Комментарий', max_length=200)