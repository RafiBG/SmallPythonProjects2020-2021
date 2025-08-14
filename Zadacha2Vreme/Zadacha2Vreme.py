from datetime import date
from datetime import datetime

today = str(date.today().strftime('%Y/%m/%d'))
print(f'Днеска е: {today}')

text = input("Въведи си рожденната дата по този пример 2003/01/22 <-- това е моята рожденна дата: ")

data = datetime.strptime(text, '%Y/%m/%d')
today = datetime.strptime(today, '%Y/%m/%d')
age_by_days = today - data

print(f'Вашата възраст в дни: {age_by_days.days}')
