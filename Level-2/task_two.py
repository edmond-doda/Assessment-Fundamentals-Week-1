"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    """Creates a new key for the dictionary - quantity - which updates if an item already in the basket is being added again."""
    for item_in_current_basket in basket:
        if ((item_in_current_basket['name'] == item['name'])
                and (item_in_current_basket['price'] == item['price'])):
            item_in_current_basket['quantity'] += 1
            return basket
    item['quantity'] = 1
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    if basket == []:
        return "Basket is empty"

    receipt = ""
    total = 0

    for item in basket:
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"] * quantity
        if price == 0:
            receipt += f"{name} x {quantity} - Free\n"
        else:
            receipt += f"{name} x {quantity} - £{price:.2f}\n"
        total += price

    receipt += f"Total: £{total:.2f}"
    return receipt

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
