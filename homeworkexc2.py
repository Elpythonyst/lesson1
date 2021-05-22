def discounted(price, discount, max_discount=20, name=''):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except ValueError:
        return 'Не могу посчитать'
    except TypeError:
        return 'Некорректный тип исходных данных'
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower():
        return price
    else:
        return price - (price * discount / 100)
    

print(discounted(100, 5))
print(discounted(100, 'bim'))