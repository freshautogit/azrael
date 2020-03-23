from django import forms


# from .models import Contact


# class ContactForm(forms.ModelForm):

#     files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

#     class Meta:
#         model = Contact
#         fields = ('name', 'phone', 'email', 'body')

class DocumentForm(forms.Form):
    userFile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))