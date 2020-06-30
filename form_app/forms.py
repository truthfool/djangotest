from django import forms
from form_app.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


def clean(self):
    all_clean_data=super().clean()
