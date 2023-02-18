from django.shortcuts import render
from .forms import TextEditorForm


def index(request):
    form=TextEditorForm()
    
    return render(request,'index.html',{'form':form})