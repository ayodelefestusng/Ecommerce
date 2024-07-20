from django import forms
from .models import Customer


class Taskform (forms.ModelForm):
    class Meta :
        model=Customer   #  The name of the databse we created on Sqlite for this proeject 
        fields = ('user','email')  # The table columns of the databse 