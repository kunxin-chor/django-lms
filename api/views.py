from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from catalog.models import Course

def find_courses(request):
   
    # courses = list(Course.objects.all().values())
    courses = Course.objects.all()
    if 'title' in request.GET:
        courses = Course.objects.filter(title = request.GET.get('title'))
    if 'desc' in request.GET:
        courses = courses.filter(desc__startswith=request.GET.get('desc'))
    serialized = list(courses.values())
    return JsonResponse(serialized, safe=False)
    