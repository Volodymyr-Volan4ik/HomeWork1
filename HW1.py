from datetime import datetime

date = "2024-12-18"

def get_days_from_today(date):

    try:

            date1 = datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
         
         return "Ошибка: Неправильный формат даты. Используйте формат YYYY-MM-DD."

    current_date = datetime.today()

    difference = current_date - date1

    return difference.days
get_days_from_today(date)
