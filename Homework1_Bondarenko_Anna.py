# Задание 1
a = 1
b = 2
print(a)
print(b)
first_name = input("Введите ваше имя:")
last_name = input("Введите вашу фамилию:")
age = int(input("Сколько вам лет?"))
print("Привет,",first_name,last_name, "!", "Тебе", age, "лет!")

# Задание 2
time = int(input("Введите время:"))
time = (
    f"{time//3600}:"
    f"{(time//60)%60}:"
    f"{time%60}"
)
print(time)

# Задание 3
n = input("Введите число:")
n1 = n + n
n2 = n + n + n
n = int(n)
n1 = int(n1)
n2 = int(n2)
a = (n + n1 + n2)
print(a)

#Задание 4
n = int(input("Введите число:"))
minn = 0
while n != 0:
    if n % 10 > minn:
        minn = n % 10
        n = n//10
print("Самая большая цифра:", minn)

#Задание 5
a = int(input("Значение выручки:"))
b = int(input("Значение издержек:"))
if a > b:
     print("Фирма отработала с прибылью")
elif a < b:
     print("Фирма отработала с убытком")

if a > b:
     n = a - b#прибыль
     m = (n/a)*100
print("Рентабельность =",m,"%")
k = int(input("Количество сотрудников:"))
p = n/k
print("Прибыль фирмы в расчете на одного сотрудника =", p)


#Задание 6
a = int(input("Количество км в первый день:"))
b = int(input("Цель:"))
count = 1

while b > a:
    count += 1
    c = a*0.1
    a = a+c
print(count)