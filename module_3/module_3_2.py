# Функция для проверки корректности e-mail
def is_valid_email(email):
    if "@" not in email: # если в имейл нет "собаки"
        return False
    # или не оканчивается на ".com"/ ".ru" / ".net"
    if not (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net")):
        return False  # возвращаем ложь
    return True # или истину, если имейл валиден


def send_email(message, recipient, *, sender="university.help@gmail.com"):

    # Проверка корректности отправителя и получателя
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Тестовые вызовы функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
