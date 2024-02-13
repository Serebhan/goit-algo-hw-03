import re

def normalize_phone(phone_number):
    pattern = r"\d+" # регулярний вираз для цифр
    ret=""
    for pat in  re.findall(pattern, phone_number): # Циклом збираємо з кусочків рядок що містить лише цифри
        ret=ret+pat
    if ret[0]=="3": # якщо номер повний залишилось лише додати + на початку
        return "+"+ret
    elif ret[0]=="8": # якщо номер не повний додаємо відповідну частку кода
        return "+3"+ret
    elif ret[0]=="0": # якщо номер не повний додаємо відповідну частку кода
        return "+38"+ret


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)