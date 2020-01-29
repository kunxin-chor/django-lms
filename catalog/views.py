from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Course
from .forms import CourseForm

# Create your views here.
def show_courses(request):
    all_courses = Course.objects.all()
    return render(request, 'catalog/courses.template.html', {
        'all_courses':all_courses
    })
    
    
def create_course(request):
    if request.method == 'POST':
        create_course_form = CourseForm(request.POST)
        if create_course_form.is_valid():
            newly_created_course = create_course_form.save()
            messages.success(request, "Course " + newly_created_course.title + " has been created!")
            return redirect(reverse(show_courses))
      
    else:
        create_course_form = CourseForm()
  
    return render(request, 'catalog/create_course.template.html', {
        'form':create_course_form
    })
    
# course_id is the name of second argument because the path is update/<course_id>
def update_course(request, course_id):
    course_being_updated = get_object_or_404(Course, pk=course_id)
    
    if request.method == "POST":
        # for update
        update_course_form = CourseForm(request.POST, instance=course_being_updated)
        if update_course_form.is_valid():
            update_course_form.save()
         
            # always make sure to return the redirect
            return redirect(reverse(show_courses))
    else:
        update_course_form = CourseForm(instance=course_being_updated)
    
    return render(request, 'catalog/update_course.template.html',{
        'form':update_course_form
    })
    
def confirm_delete_course(request, course_id):
    course_being_deleted = get_object_or_404(Course, pk=course_id)
    return render(request, 'catalog/confirm_delete_course.template.html', {
        'course':course_being_deleted
    })


def actually_delete_course(request, course_id):
    course_being_deleted = get_object_or_404(Course, pk=course_id)
    course_being_deleted.delete()
    return redirect(reverse('show_courses'))