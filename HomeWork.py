from datetime import datetime, date, timedelta
import random
import re

'''
first homework
'''


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today_day = datetime.now()
        return today_day.toordinal() - date.toordinal()
    except ValueError:
        print("Please enter in format YYYY-MM-DD: ")  
print(get_days_from_today("2022-11-11"))




'''
second homework
'''


def get_numbers_ticket(min, max, quantity):
    try:
        random_list_of_numbers = list(range(min, max+1))
        finally_numbers = list(sorted(random.sample(random_list_of_numbers, k=quantity)))
        return finally_numbers
    except ValueError:
        print("You need to enter three numbers: minimum, maximum and quantity(must be <= maximum). Please try again: ")
      
lottery_numbers1 = get_numbers_ticket(10, 14, 6)
print(f"Your lottery numbers: {lottery_numbers1}")



'''
third homework    #  py HomeWork.py
'''

def normalize_phone (phone_number):
    new_number1 = re.sub(r"\D","", phone_number) # delete all symbols 
    UAcod1 = "+38"
    UAcod = "+"
    new_number = re.search(r"^38", new_number1) # if number has 38 
    if new_number == None:
        return UAcod1+new_number1
    else:
        return UAcod+new_number1


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

