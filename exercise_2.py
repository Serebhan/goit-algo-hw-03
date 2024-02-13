import random
numberList=list(range(1, 1001)) # Створення найбільшого можливого списку чисел.

def get_numbers_ticket(min, max, quantity): 
    if min in numberList and max in numberList and quantity <= max-min : # Перевірка умов валідності введених даних.
        population =numberList[min-1:max] # Формування вирізки з загального списку списку за заданим діапазоном
        return sorted(random.sample(population, quantity)) # видобування та сортування відповідної кількості випадкових значень із списку можливих
    else:
        return ""


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)