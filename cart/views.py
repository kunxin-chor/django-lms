from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# importing the Course model from the catalog app
from catalog.models import Course

# Create your views here.
def add_to_cart(request, course_id):
    # we are going to add the course specified by the course_id argument to cart
    course = get_object_or_404(Course, pk=course_id)
    
    # get the object specified by the key 'shopping_cart'
    # if not found, return an empty dictionary
    cart = request.session.get("shopping_cart", {})
    
    # if the course has not been added to cart before
    if course_id not in cart:
        cart[course_id] = {
            'title': course.title,
            'id':course.id,
            'cost':99
        }
        # save the cart back to the session under the key 'shopping_cart'
        request.session['shopping_cart'] = cart
        messages.success(request, "You have added a new course")
    else:
        messages.success("The course is already in your shopping cart")
    return redirect('/catalog/')
 
    
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html',{
        'cart':cart
    })
    
def remove_from_cart(request, course_id):
    cart = request.session.get('shopping_cart', {})
    
    if course_id in cart:
        del cart[course_id]
        request.session['shopping_cart'] = cart
        messages.success(request, 'Course has been removed')

    return redirect(view_cart)
        
    