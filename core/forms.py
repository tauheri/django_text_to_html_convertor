from django import forms
from .models import TextEditor
from ckeditor.widgets import CKEditorWidget




class TextEditorForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    
    class Meta:
        model=TextEditor
        fields="__all__"