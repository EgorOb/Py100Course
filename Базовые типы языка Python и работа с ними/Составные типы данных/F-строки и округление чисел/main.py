name = "Анна"
age = 25
print(f"Привет, меня зовут {name} и мне {age} лет.")  # Вставка переменных внутрь текста

x = 10
y = 3
print(f"Сумма чисел {x} и {y} равна {x + y}.")  # Внутри f-строк можно делать вычисления

number = 3.14159
print(f"Число Пи: {number:.2f}")  # Округление числа до двух знаков после запятой


data = [{"name":"user", "age": "10"}, {"name":"user1", "age": "11"}, {"name":"user2", "age": "12"}]
print(f"|{'Имя':>20}|{'Возраст':>20}|")
print("_"*43)
for person in data:
    print(f"|{person['name']:^20}|{person['age']:^20}|")
print("_"*43)


