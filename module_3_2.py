def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif recipient != sender:
        count = 0
        dot = ['.com', '.net', '.ru']
        for i in dot:
            if i in recipient and sender:
                count = 0 + 1
        if count > 0 :
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:  print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email('Привет', 'pavel@gmail.com')
