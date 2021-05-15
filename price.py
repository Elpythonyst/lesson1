def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'
a = get_summ('Learn', 'Python')
print(a.upper())

def format_price(price):
    return f'Цена: {int(price)} руб.'
b = format_price(56.24)
print(b)