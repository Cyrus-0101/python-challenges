"""
    Write a new function that passes in a credit card number
    and returns a masked number. Only show the last 4 digits of
    the credit card number

    Notes/Constraints:

    * Cards may have different amount of numbers. 

"""

def mask_credit_card(card_number):
    """
    :param card_number:
    :return:
    """
    return "XXXX-XXXX-XXXX-{}".format(card_number[-4:])

print(mask_credit_card("1234567890123456"))

# Sol 1

## Step 1

credit_card_str = "1234123412341234"

string_length = len(credit_card_str)

mask = string_length - 4

show_str = credit_card_str[mask:]

print(("*" * mask) + show_str)


## Step 2

def masking(credit_card_number, numbers_to_mask):
    
    nums_to_mask = ''

    n = numbers_to_mask

    for i in credit_card_number[:-n]:
        
        nums_to_mask += '*'

    nums_to_mask += credit_card_number[-n:]

    return nums_to_mask

print(masking("1234123412341234", 4))

# Sol 2

credit_card_str = "1234123412341234"

masked_number = credit_card_str[-4:].rjust(len(credit_card_str), '*')

print(masked_number)


# Sol 3 (Hacky)

credit_card_str = "12341234123412345678"

masked_number = '*' * 12 + credit_card_str[-4:]

print(masked_number)
