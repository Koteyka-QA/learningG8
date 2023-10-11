# TASK1.   Створити функцію, що приймає число з консолі (використати функцію input());
#   Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int()
#   спробувати конвертувати рядок в число (input() завжди повертає рядок). Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data".
# noinspection PyUnreachableCode
def process_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Entered not valid data")


# TASK2 Створити функцію, що приймає 2 рядки;
# Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки),
# якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.
def process_strings(str1, str2):
    try:
        num1 = int(str1)
        num2 = int(str2)
        return = num1 + num2
    except ValueError:
        concatenated = str1 + str2
        print("Concatenated:",concatenated)

# TASK3 Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
# тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
# Коли користувач вводить число, дякуємо йому

def get_valid_number_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = int(user_input)
            print("Thank you!:)")
            return number
        except ValueError:
            print("Please enter a valid number.")

# TASK4 Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
# Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його (return)

class OnlyEvenError(Exception):
    pass
def check_digit(number):
    if number % 2 != 0:
        raise OnlyEvenError("Number must be even")
    return number

# TASK5 Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit, в яку передавати це число.
#   Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1. Інакше, помножити число на 2.
#   Результат виводити в консоль.
#   Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую".
#   Використовувати try-except-else-finally

def process_and_print_result(number):
    try:
        result = check_digit(number)
    except OnlyEvenError:
        number += 1
    else:
        number *= 2
    finally:
        print("I always print something")
    print("Result:", result)
