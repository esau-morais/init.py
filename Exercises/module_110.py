def increase(price=0, p=0, simbol=False):
    final = price + (price * p / 100)
    return final if simbol is False else money(final)


def decrease(price=0, p=0, simbol=False):
    final = price - (price * p / 100)
    return final if simbol is False else money(final)


def double(price=0, simbol=False):
    final = price * 2
    return final if not simbol else money(final)


def half(price=0, simbol=False):
    final = price / 2
    return final if not simbol else money(final)


def money(price: float=0, m="R$"):
    return f"{m}{price}".replace(".", ",")

def summary(price = 0, pi=20, pd=12):
    print("-" * 32)
    print(" == SUMMARY OF THE VALUE == ".center(32))
    print("-" * 32)
    print(f"Entered price: \t\t{money(price)}")
    print(f"Double: \t\t{double(price, True)}")
    print(f"Half: \t\t\t{half(price, True)}")
    print(f"Increasing {pi}%: \t{increase(price, pi, True)}")
    print(f"Decreasing {pd}%: \t{decrease(price, pd, True)}")
    print("-" * 32)

