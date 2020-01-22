from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=('title', 'desc', 'number_of_hours', 'instructor')
        
    