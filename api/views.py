from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from catalog.models import Course

def find_courses(request):
   
    # courses = list(Course.objects.all().values())
    # courses = Course.objects
    courses = Course.objects
    if len(request.GET) == 0:
        courses = courses.all()
    if 'title' in request.GET:
        courses = courses.filter(title__contains = request.GET.get('title'))
    if 'desc' in request.GET:
        courses = courses.filter(desc__contains=request.GET.get('desc'))
    # courses = courses.filter(title__in=['React 101'])
    serialized = list(courses.values())
    return JsonResponse(serialized, safe=False)
    