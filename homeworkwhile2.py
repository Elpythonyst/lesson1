homedict = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'Какой сегодня год?': '2021'}

def ask_user():
    while True:
        user_msg = input('Введите вопрос: ')
        print(f'{homedict.get(user_msg, "Не везёт")}')
        return 

ask_user()