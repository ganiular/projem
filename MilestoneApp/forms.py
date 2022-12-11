from django import forms
from .models import Project, Student


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(max_length=25,
                                   widget=forms.TextInput(attrs={'class': 'input', 'id': 'name'}))
    project_detail = forms.CharField(max_length=150,
                                     widget=forms.TextInput(attrs={'class': 'input', 'id': 'detail'}))
    project_image = forms.ImageField(required = False,
                                     widget=forms.FileInput(attrs={'class': 'input-img', 'id': 'image'}))

    class Meta:
        model = Project
        fields ='__all__'


class StudentForm(forms.ModelForm):
    student_name = forms.CharField(max_length=50,
                                   widget=forms.TextInput(attrs={'class': 'input'}))
    student_project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                             empty_label='',
                                             widget=forms.Select(attrs={'class': 'input', 'id': 'selection'}))
    student_deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'input'}))
    
    class Meta:
        model = Student
        fields = '__all__'