age = int(input('Введите ваш возраст: '))


def occupation(age):
    if age <= 6:
        return 'Завтра в садик'
    elif 6 < age <= 17:
        return 'Завтра в школу'
    elif 17 < age <= 23:
        return 'Завтра в университет'
    else:
        return 'Опять работать'

my_mental_age = occupation(25)
print(my_mental_age)