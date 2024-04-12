from datetime import datetime, date, timedelta
import random

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
    random_list_of_numbers = list(range(min, max+1))
    finally_numbers = list(sorted(random.sample(random_list_of_numbers, k=quantity)))
    return finally_numbers

lottery_numbers1 = get_numbers_ticket(1, 49, 6)
print(f"Your lottery numbers: {lottery_numbers1}")



