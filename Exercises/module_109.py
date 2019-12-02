def increase(price=0, simbol=False):
    p1 = (10/100) * price
    final = price + p1
    return final if simbol == False else money(final)


def decrease(price=0, simbol=False):
    p2= (13/100) * price
    final = price - p2
    return final if simbol == False else money(final)


def double(price=0, simbol=False):
    final = price * 2
    return final if simbol == False else money(final)


def half(price=0, simbol=False):
    final = price / 2
    return final if simbol == False else money(final)


def money(price, m="R$"):
    return f"{m}{price}"

