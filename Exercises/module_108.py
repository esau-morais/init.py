def increase(price):
    p1 = (10/100) * price
    i = price + p1
    return i

def decrease(price):
    p2= (13/100) * price
    d = price - p2
    return d

def double(price):
    return price * 2


def half(price):
    return price / 2


def money(price):
    return f"R${price}"

