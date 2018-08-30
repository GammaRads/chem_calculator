def input_is_digit(value):
    cont = value.isdigit()
    while not cont:
        print("Integer values only:")
        value = input()
        cont = value.isdigit()
    return value


def input_is_decimal(value):
    cont = False
    while not cont:
        try:
            float(value)
            cont = True
        except ValueError:
            print("Numeric values only:")
            value = input()
            cont = False
    return value
