# Задание №1:
# Даны три числа. Вывести на экран “yes”, если среди них
# есть одинаковые, иначе вывести “ERROR”;
print('Задание №1:')
import random as r

a = []
b = []
c = []
for _ in range(r.randint(1, 1)):
	a.append(r.randint(1, 4))
	b.append(r.randint(2, 4))
	c.append(r.randint(3, 4))
print(a, b, c)

if a == b == c:
	print('YES')
else:
	print('ERROR')

print('___ ___ ___ ___ ___ ___ ___')
print()
# Задание №2:
# Даны три числа. Вывести на экран “yes”, если можно взять
# какие-то два из них и в сумме получить третье;
print('Задание №2:')

a = []
b = []
c = []
for _ in range(1):
	a.append(r.randint(1, 5))
	b.append(r.randint(1, 5))
	c.append(r.randint(1, 5))
print(a, b, c)

if a[0] + b[0] == c[0] or a[0] + c[0] == b[0] or b[0] + c[0] == a[0]:
	print('Yes')
else:
	print('ERROR')

print('___ ___ ___ ___ ___ ___ ___')
print()
# Задание №3:
# Посчитать сумму числового ряда от 0 до 14 включительно.
# Например, 0+1+2+3+…+14;
print('Задание №3:')

summa = 0
for i in range(0, 15):
	summa += i
print('Summa =', summa)


print('___ ___ ___ ___ ___ ___ ___')
print()
# Задание №4:
# Распечатывать дни недели с их порядковыми номерами.
# Кроме того, рядом выводить выходной ли это день или рабочий.
print('Задание №4:')

num_week_days = {'1.':'Mon':'working_day',
				'2.':'Tue':'working_day',
				'3.':'Wed':'working_day',
				'4.':'Thu':'working_day',
				'5.':'Fri':'working_day',
				'6.':'Sat':'weekend',
				'7.':'Sun':'weekend'}
for day in num_week_days:
	print("The number %s day %s is %s" % (day, num_week_days[day]))