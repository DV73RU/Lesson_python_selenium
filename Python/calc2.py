"""Калькулятор"""


add_fn = "Какие действия с числами выполнить? "
fn = ["/", "*", "+", "-", "x", "p"]  # Список функций
fn_ok = "Есть такая функция"

val_err = "Это не число"

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
except ValueError:
    
    print(f"{input} + {val_err}")  # Обработка ошибки в ведения символа отличного от числа.
else:
    print(add_fn)   # Печатаем текст выбора действия с цифрами
    inn = input(
        "Нажмите:\n'/' - деление,\n'*' - умножение,\n'+' - сложение,\n'-' - вычитание,\n'x' - выход\n")
    # Проверяем отсутствие элемента в списке с символом введённого с клавиатры.
    if inn not in fn:
        # Выводим текст о не неправильном ввода функции и введенный символ.
        print(f"{inn} <- " + fn_err)
    # Проверяем символ введённый с клавиатуры присутствует в списке функций.
    if inn == "/" in fn:
        # Выводим текст о присутствии такой функции в списе и введённый символ.
        print(f"{inn} <- " + fn_ok)
        try:
            result = int(a / b)     # Производим деление переменных.
        except ZeroDivisionError:   # Обработка ошибки деления на ноль.
            result = 0
            # Выводим текст если делили но ноль.
            print("\033[4m\033[37m\033[41m{}\033[0m".format(
                "На ноль делить нельзя"))
        else:
            # Текст результата деления на ноль
            print(f"Результат деления: {a} на {b} равен: {result}")
    # Проверяем символ введённый с клавиатуры присутствует в списке функций.
    elif inn == "*" in fn:
        # Выводим текст о присутствии такой функции в списе и введённый символ.
        print(f"{inn} <- " + fn_ok)
        result = int(a * b)
        print(f"Результат умножение: {a} на {b} равен: {result}")
    # Проверяем символ введённый с клавиатуры присутствует в списке функций.
    elif inn == "+" in fn:
        # Выводим текст о присутствии такой функции в списе и введённый символ.
        print(f"{inn} <- " + fn_ok)
        result = int(a + b)
        print(f"Результат сложения: {a} и {b} равен: {result}")
    # Проверяем символ введённый с клавиатуры присутствует в списке функций.
    elif inn == "-" in fn:
        # Выводим текст о присутствии такой функции в списе и введённый символ.
        print(f"{inn} <- " + fn_ok)
        result = int(a - b)
        print(f"Результат вычитания: {b} из {a} равен: {result}")
    # Проверяем символ введённый с клавиатуры присутствует в списке функций.
    elif inn == "х" in fn:
        # Выводим текст о присутствии такой функции в списе и введённый символ.
        print(f"{inn} - " + fn_ok)
        quit()  # Выход из скрипта
