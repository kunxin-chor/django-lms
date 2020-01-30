def cart_contents(request):
    # make the content of the shopping cart available to all templates
    cart = request.session.get("shopping_cart", {})
    return {
        'shopping_cart':cart,
        'number_of_items':len(cart)
    }