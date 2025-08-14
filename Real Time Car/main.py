import datetime
from datetime import date
import dateutil.parser
from termcolor import colored

today = date.today()
validnost_na_vinetka = datetime.date(2021, 2, 2)
validnost_na_tehnicheski_pregled = datetime.date(2021, 2, 1)
validnost_na_zastrahovka = datetime.date(2021, 1, 30)


new_dateA = validnost_na_vinetka - today
new_dateB = validnost_na_tehnicheski_pregled - today
new_dateC = validnost_na_zastrahovka - today


print ('Оставащи дни за валидност на винетка:',new_dateA)
print ('Оставащи дни за валидност на технически преглед: ', new_dateB)
print ('Оставащи дни за застраховка:', new_dateC)

if  new_dateA.days>30:
    print ('')

else:
    print ('')
    print (colored('ВНИМАНИЕ ОСТАВАТ ВИ ОТ ВАЛИДНОСТ НА ВИНЕТКА :','red') ,new_dateA)

if  new_dateB.days>30:
    print ('')

else:
    print (colored('ВНИМАНИЕ ОСТАВАТ ВИ ОТ ТЕХНИЧЕСКИ ПРЕГЛЕД :','red') ,new_dateB)

if  new_dateC.days>30:
    print ('')

else:
    print (colored('ВНИМАНИЕ ОСТАВАТ ВИ ОТ ЗАСТРАХОВКА :','red') ,new_dateC)

