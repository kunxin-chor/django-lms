from django import forms
from .models import Course
from pyuploadcare.dj.forms import ImageField

class CourseForm(forms.ModelForm):
    image = ImageField(label="Cover Image")
    class Meta:
        model=Course
        fields=('title', 'desc', 'number_of_hours', 'instructor', 'image')
        
    