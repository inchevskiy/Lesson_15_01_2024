def calculator():
    while True:
        try:
            # Введення математичного виразу
            expression = input("Введіть математичний вираз: ")

            # Обчислення та виведення результату
            result = eval(expression)
            print("Результат:", result)
        except Exception as e:
            print("Помилка :", e)

        # Запитання користувача про продовження роботи
        user_input = input("Продовжити роботу калькулятора? (y/n): ").lower()
        if user_input != 'y':
            break


# Запуск калькулятора
calculator()
