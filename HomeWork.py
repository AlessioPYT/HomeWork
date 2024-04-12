from datetime import datetime, date, timedelta


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today_day = datetime.now()
        return today_day.toordinal() - date.toordinal()
    except ValueError:
        print("Please enter in format YYYY-MM-DD: ")  

print(get_days_from_today("2022.11.11"))
