import string
import keyword

def is_valid_variable_name(variable_name):
    return (
        variable_name[0].isalpha() and
        all(char.isalnum() or char == '_' for char in variable_name) and
        variable_name not in keyword.kwlist and
        variable_name.count('_') == 1 and
        variable_name != "_"
    )

# Введення рядка від користувача
user_input = input("Введіть ім'я змінної: ")

# Виведення результату перевірки
print(is_valid_variable_name(user_input))
