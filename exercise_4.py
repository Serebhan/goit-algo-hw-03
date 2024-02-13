from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.07"},
    {"name": "Jane Smith", "birthday": "1990.02.10"},
    {"name": "Banny Doe", "birthday": "1985.02.06"},
    {"name": "Banny Smith", "birthday": "1990.02.08"},
    {"name": "John Boss", "birthday": "1985.02.09"},
    {"name": "Kurva Bober", "birthday": "1985.02.01"},
    {"name": "Jane Boss", "birthday": "1990.02.13"}
]

# Маємо блок викликів різних функцій що роблять кожна невеличку задачу задля того щоб в основній функції було мало тексту і зрозуміло що вона робить.

def get_list_of_week(): # формуємо список дат днів на найближчі 7 днів від поточної дати
    week=[]
    delta = timedelta(days=1)
    week.append(datetime.now().strftime(".%m.%d"))
    for i in range (1,7):
        week.append((datetime.now()+delta*i).strftime(".%m.%d"))
        
    return week

def get_list_of_weekend_and_monday(): # В цьому блоці формуємо списки для дат суботи та неділі на поточному тижні, а також вираховуємо дату найближчого понеділка, нвіть якщо він не на поточному тижні.
    weekend=[]
    monday=[]
    delta = timedelta(days=1)
    for i in range (8):
        if ((datetime.now()+delta*i).weekday())>=5:
            weekend.append((datetime.now()+delta*i).strftime(".%m.%d"))
        if len(weekend)==2 and ((datetime.now()+delta*i).weekday())==0:
            monday.append((datetime.now()+delta*i).strftime(".%m.%d"))
    return weekend, monday

def we_hawe_birthday_in_weekend(data, weekend): # Перевіряємо чи не на вихідний припадає дата
    if data[-6:] in weekend:
        return True
    else:
        return False

def we_have_birthday(data, week): # Перевіряємо чи на цьому тижні є іменинники просто порівнюючи певну дату із списком.
    if data[-6:] in week:
        return True
    else:
        return False
    
# Основна функція

def get_upcoming_birthdays (users):  # Основна функція  - з неї робим виклики відповідних блоків коду, формуємо список словників з датами поздоровлень
    week=get_list_of_week()
    weekend, monday=get_list_of_weekend_and_monday()
    congratulations=[]
    for user in users:
        if we_have_birthday(user["birthday"], week):
            if we_hawe_birthday_in_weekend(user["birthday"], weekend ):
                user["congratulations_date"]=(datetime.now().strftime("%Y")) + monday[0]
                del user["birthday"]
                congratulations.append(user)
            else:
                user["congratulations_date"]=(datetime.now().strftime("%Y")) + user["birthday"][-6:]
                del user["birthday"]
                congratulations.append(user)
    return congratulations

# Можливий виклик основної функції

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)