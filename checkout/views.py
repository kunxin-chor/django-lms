from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from catalog.models import Course


# Create your views here.
def checkout(request):
    # print(settings.STRIPE_SECRET_KEY)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # retrieve shopping cart
    cart = request.session.get('shopping_cart', {})
    
    line_items = []
    
    # generate the line_items
    for id,course in cart.items():
        # For each item in the cart, get its details from the database
        course = get_object_or_404(Course, pk=id)
        line_items.append({
            'name': course.title,
            'amount': int(course.cost*100), #convert to cents, in integer
            'currency':'usd',
            'quantity':1
        })
    
    #generate the session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
        payment_intent_data={
            'capture_method':'manual'
        }
    )
    
    # render the template
    return render(request, 'checkout/checkout.template.html', {
        'session_id':session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
def checkout_success(request):
    return HttpResponse("Checkout success")
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")