def find_unique_value(some_list):
    # Створюємо словник, де ключами будуть числа, а значеннями - їх кількість в початковому списку
    counts = {}
    for num in some_list:
        counts[num] = counts.get(num, 0) + 1

    # Шукаємо унікальне число, яке має значення 1 в словнику
    for num, count in counts.items():
        if count == 1:
            return num


# Тести
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
