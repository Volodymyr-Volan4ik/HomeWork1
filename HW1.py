from datetime import datetime

def get_days_from_today():
        try:
            current_date = datetime.today()

            user_input = input("Введите дату в формате ГГГГ-ММ-ДД: ")

            user_date = datetime.strptime(user_input, "%Y-%m-%d")

            difference = current_date - user_date

            print(f"Разница между сегодня и введенной датой: {difference} дней")

            get_days_from_today()

        except ValueError:

            print("Ошибка: Неправильный формат даты. Используйте формат ГГГГ-ММ-ДД.")

            get_days_from_today()

get_days_from_today()