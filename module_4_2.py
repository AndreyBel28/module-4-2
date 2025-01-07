#Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

test_function()

try:
    inner_function()  # Это вызовет ошибку
except NameError as e:
    print(e)

