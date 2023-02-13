from django import forms

from .models import Game, Comment



# class GameSearchForm(forms.Form):
#     game_name = forms.CharField(
#         max_length=50, help_text="Enter searched game", widget=forms.Textarea(attrs={'class':'form-control'}))
    
#     game_name.widget.attrs.update({'class': 'form-control'})



# class CommentModelForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         widgets = {
#             'text':forms.Textarea(attrs = {'cols': 80, 'rows': 20}),
#         }
#         labels = {
#             'text': 'Comment text',
#         }
#         help_texts = {
#             'text': 'Пожалуйста, введите текс'
#         }

            

            
