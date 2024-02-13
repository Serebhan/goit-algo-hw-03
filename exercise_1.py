from datetime import datetime

now = (datetime.now()).toordinal() #Встановлюємо номер дня на поточну дату

def get_days_from_today(date):
    try:
        return now -(datetime.strptime(date, "%Y-%m-%d")).toordinal() # Обчислюємо різність номеру дня для поточної дати та дати що ввели
    except ValueError:
        return None # В разі якщо не вдалося обрахувати різність вертаемо невизначеність.
        

     

print (get_days_from_today("2020-10-09"))