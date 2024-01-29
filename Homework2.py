def calculator():
    while True:
        print("Введіть операцію (+, -, *, /) або 'вихід' для виходу")
        operation = input()

        if operation == 'вихід':
            break

        if operation in ('+', '-', '*', '/'):
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))

            if operation == '+':
                print(num1 + num2)
            elif operation == '-':
                print(num1 - num2)
            elif operation == '*':
                print(num1 * num2)
            elif operation == '/':
                if num2 != 0:
                    print(num1 / num2)
                else:
                    print("Помилка: Ділення на нуль неможливе!")
        else:
            print("Помилка: Неправильна операція!")

calculator()
