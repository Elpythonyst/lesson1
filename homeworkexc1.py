def hello_user():
    while True:
        try:
            user_input = input('Как дела? ')
            if user_input == 'Хорошо':
                print('Ну и отлично')
                return
            else:
                print('Нет, твои дела не таковы')
        except KeyboardInterrupt:
            print('\nПока!')
            break

hello_user()