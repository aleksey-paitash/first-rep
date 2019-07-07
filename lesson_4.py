# Конструкция while
money = 10
while money > 0:
	print('We have ' + str(money) + ' dollars')
	money -= 1
while money == 0:
	print('No more money, time to work')
	break
print()

# Бесконечный цикл
#   num = 1
#   while num < 10:
#   	print('Jason Statham')
#   	break  # принудительное завершение цикла

# Как остановить бесконечный цикл?
#   - Esc
#   - Сtrl + c
#   - Break
#   - Alt + f4  :D
#   - Лоу-кик или клинч :D

# Создадим цикл while
password = ''
while password != 'password':
	print('What is the Password?')
	password = input()

print('Yes, the password is ' + password + '. You may Enter')
print()

#  Запись цикла while в Python выглядит так:
#  while [условие истинно]:
#   [сделать указанное]

# Простой пример использования этого цикла:
count = 0
while count < 6:
	print(count)
	count += 2
print(count)
print()

# Напишем простую игрушку при помощи цикла while
# Программа будет генерировать случайное число, пользователь
# должен угадать это число.

import random
number = random.randint(1, 25)
# записываем в переменную случайное число в диапазоне
# от 1 до 25

guesses = 0

while guesses < 5:
	print('LOSE!')
	break
if guesses == number:
	print('WIN')
#	break    - выдает ошибку
print()

#  Цикл For
print('Primer #1:')
word = "agent"  # строка word
bag = ["knife","handgun","camera","notebook"]  # список bag
countries = {"Swiss":"Bern", "Ukrain":"Kiev",
			"Italy":"Rome", "Australia":"Canberra",
			"Japan":"Tokyo"}   # словарь countries

for letter in word:
	print(letter)
for item in bag:
	print(item)
for country in countries:
	print("The capital of %s is %s" % (country, countries[country]))
print()

print('Primer #2:')
week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for i in range(len(week_days)):
	print(week_days[i])
print()

# Циклы могут быть вложенными
# Вот пример создания двумерного списка и вывода его на экран с помощью print.

d = [[1,2,3],[4,5,6]]
for q in range(2):
	for j in range(3):
		print(d[q][j])
print()

# Цикл Break
metals = ['Cu', 'Fe', 'Al', 'Au', 'U', 'Mg']
for item in metals:
	print(item)
	if item == 'Au':
		print('Ура! Я нашел золото!')
		break
print()

age = 60
while True:
	print('Мой возраст %s. Должен ходить на работу ' % age)
	age +=1
	if age > 65:
		print('Ура! Наконец-то пенсия!')
		break
print()

# Цикл Continue.
# Другая инструкция, которая может менять цикл,
# – это continue. Если она указана внутри кода, то все
# оставшиеся инструкции до конца цикла пропускаются и
# начинается следующая итерация.

# Цикл Pass.
# С оператором pass программа работает так, будто в ней
# нет условных операторов. Оператор pass говорит программе
# игнорировать это условие и продолжать работу. 

# Вернемся к игре про числа:
import random as r
number = r.randint(1, 25)
guesses = 0
while guesses < 5:
	print('Guess a num between 1 and 25:')
	guess = input()
	guess = int(guess)
	guesses += 1
	if guess < number:
		print('Too low, try again')
	if guess > number:
		print('Too high, try again')
	if guess == number:
		print('You guesses the number in ' + str(number) + ' tries!')
		print('You WIN!')
		break
else:
	print('You did not guesses the number, it was ' + str(number))

print()
