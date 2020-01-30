from django.shortcuts import render, reverse, HttpResponse
import stripe

from catalog.models import Course


# Create your views here.
def checkout(request):
    # retrieve shopping cart
    cart = request.get('shopping_cart', {})
    
    line_items = []
    
    # generate the line_items
    for id,course in cart.items:
        course = get_object_or_404(Course, pk=id)
        line_items.append({
            'id': course.id
            'title': course.title,
            'cost': course.cost
        })
    
    session_id = stripe.checkout.session.Create(
        payment_methods=['card'],
        line_items=line_items,
        success_url=reverse(checkout_success),
        cancel_url=reverse(checkout_cancelled)
    )
    
    # render the template
    return render(request, 'checkout/checkout.template.html', {
        'session_id':session_id
    })
    
def checkout_success(request):
    return HttpResponse("Checkout success")
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")