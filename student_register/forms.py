from django import forms
from .models import Students

class StudentForm(forms.ModelForm):

    class Meta:
        model= Students
        fields=('fullname','mobile','sid','roles')
        labels={
            'fullname':'Full Name',
            'sid':'Student ID'
        }

    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['roles'].empty_label="Select"
        self.fields['roles'].required=False