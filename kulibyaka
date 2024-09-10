mkdir random_number_generator
cd random_number_generator
git init
git add .
git commit -m "Инициализация проекта: создание директории и инициализация Git-репозитория"
# random_number_generator.py
import random

def generate_random_number():
    return random.randint(1, 11)

if __name__ == "__main__":
    number = generate_random_number()
    print(f"Случайное число: {number}")
git add random_number_generator.py
git commit -m "Добавление основного кода: генерация случайного числа от 1 до 11"
def save_number_to_file(number):
    with open("numbers.txt", "a") as file:
        file.write(f"{number}n")

if __name__ == "__main__":
    number = generate_random_number()
    print(f"Случайное число: {number}")
    save_number_to_file(number)
git add random_number_generator.py
git commit -m "Добавление функции сохранения сгенерированного числа в файл"
def generate_random_numbers(count):
    return [generate_random_number() for _ in range(count)]

if __name__ == "__main__":
    count = int(input("Сколько чисел сгенерировать? "))
    numbers = generate_random_numbers(count)
    for number in numbers:
        print(f"Случайное число: {number}")
        save_number_to_file(number)
git add random_number_generator.py
git commit -m "Добавление функции генерации нескольких случайных чисел"
if __name__ == "__main__":
    while True:
        try:
            count = int(input("Сколько чисел сгенерировать? "))
            if count > 0:
                break
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Неправильный ввод. Пожалуйста, введите число.")

    numbers = generate_random_numbers(count)
    for number in numbers:
        print(f"Случайное число: {number}")
        save_number_to_file(number)
git add random_number_generator.py
git commit -m "Добавление обработки ввода для правильного ввода числа пользователем"
# Random Number Generator

## Описание
Программа генерирует случайные числа от 1 до 11 и сохраняет их в файл.

## Установка
1. Убедитесь, что Python установлен.
2. Клонируйте репозиторий.
3. Запустите random_number_generator.py.

## Использование
Введите количество случайных чисел для генерации.
git add README.md
git commit -m "Добавление файла README.md с описанием проекта"
mkdir src
mv random_number_generator.py src/
# main.py
from src.random_number_generator import generate_random_numbers, save_number_to_file

def main():
    # Обработка ввода пользователя
    ...

if __name__ == "__main__":
    main()
git add src/random_number_generator.py main.py
git commit -m "Структурирование проекта: разделение кода на модули"
