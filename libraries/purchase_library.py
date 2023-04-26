def calculate_total_price(purchase):
    """
    Calculates the total price of a purchase.
    """
    total_price = sum(item.price for item in purchase.get_items_list)
    return total_price
def format_phone_number(phone_number):
    """
    Formats a phone number in the format XXX-XXX-XXXX.
    """
    return f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
