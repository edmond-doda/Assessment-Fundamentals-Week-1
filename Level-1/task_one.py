
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    """Adds an item dictionary to the list call basket"""
    basket.append(item)
    return basket


def generate_receipt(full_basket: list) -> str:
    """Outputs a formatted receipt which shows the name and price of each item in a basket, as well as a total"""
    if full_basket == []:
        return "Basket is empty"

    receipt = ""
    total = 0

    for item in full_basket:
        name = item["name"]
        price = item["price"]
        if price == 0:
            receipt += f"{name} - Free\n"
        else:
            receipt += f"{name} - £{price:.2f}\n"
        total += price

    receipt += f"Total: £{total:.2f}"
    return receipt


if __name__ == "__main__":
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
