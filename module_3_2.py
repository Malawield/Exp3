def is_valid_email(email):
    valid_domains = ['.com', '.ru', '.net']
    if '@' not in email:
        return False
    for domain in valid_domains:
        if email.endswith(domain):
            return True
    return False


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not (is_valid_email(sender) and is_valid_email(recipient)):
        print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
        return
    if sender == recipient or recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса <', sender, '> на адрес <', recipient, '>')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса <', sender, '> на адрес <', recipient, '>')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
