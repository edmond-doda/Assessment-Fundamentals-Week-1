"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.

We have a string in receipt format

Want to extract the price in the receipt as separate elements that we can work with.
ideas - for each new line in the string, split after the £. Then store as a dictionary {str : float}.
"""


def generate_invoice(receipt_string: str) -> str:
    """Collects names and vat prices for all items and displays the information in an invoice format showing total exc vat, total vat amount, and total inc vat"""
    receipt_split = appends_vat_adjusted_price(receipt_string)
    vat_receipt = "'''\nVAT RECEIPT\n\n"
    total_exc_vat = 0
    total_inc_vat = 0
    for item in receipt_split:
        name = item[0]
        vat_inc_price = item[1]
        vat_exc_price = item[2]
        vat_receipt += f'{name}£{vat_exc_price:.2f}\n'
        total_exc_vat += vat_exc_price
        total_inc_vat += vat_inc_price
    vat_receipt += f"\nTotal: £{total_exc_vat:.2f}\nVAT: £{total_inc_vat-total_exc_vat:.2f}\nTotal inc VAT: £{total_inc_vat:.2f}\n'''"
    return vat_receipt  # return the invoice string


def itemises_receipt(receipt_string: str) -> list:
    """Splits each line into a list and adds that to a list. [[string, float],[string, float]...]"""
    receipt_split = []
    for line in receipt_string.splitlines():
        if 'Total: £' in line:
            continue
        elif '£' in line:
            receipt_split.append(line.split('£'))
        else:
            continue
    for item in receipt_split:
        item[1] = float(item[1])
    return receipt_split


def appends_vat_adjusted_price(receipt_string):
    """Appends a vat adjusted price to the end of the split receipt list"""
    vat_rate = 0.2
    receipt_split = itemises_receipt(receipt_string)
    for item in receipt_split:
        item.append(item[1]*(1-vat_rate))
    return receipt_split


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
