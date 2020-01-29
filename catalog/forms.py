from django import forms
from .models import Course
from pyuploadcare.dj.forms import ImageField, FileWidget

class CourseForm(forms.ModelForm):
    image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
    class Meta:
        model=Course
        fields=('title', 'desc', 'number_of_hours', 'instructor', 'image')
        
    