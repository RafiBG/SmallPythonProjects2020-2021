grade = float(input('Enter your grade:'))
if grade >= 5.50 and grade <= 6:
    print ('Отличен')
elif grade >= 2 and grade <= 3:
    print('слаб')
elif grade >= 3 and grade < 3.50:
    print('среден')
elif grade >= 3.50 and grade < 4.50:
    print('добър')
elif grade >= 4.50 and grade < 5.50:
    print('мн.добър')
else:
    print('Невалидна оценка')
