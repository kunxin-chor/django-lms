
def cart_contents(request):
    cart = request.session.get('shopping_cart', {})
    return ({
        'cart' : cart,
        'number_of_items': len(cart)
    })