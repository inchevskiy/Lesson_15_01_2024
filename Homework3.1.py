def move_last_to_first(lst):
    # Перевірка, чи список порожній або має лише один елемент
    if len(lst) <= 1:
        return lst  # Повертаємо список без змін

    # Видаляємо останній елемент і додаємо його на початок списку
    last_element = lst.pop()
    lst.insert(0, last_element)

    return lst

# Приклади використання
print(move_last_to_first([12, 3, 4, 10]))  # [10, 12, 3, 4]
print(move_last_to_first([1]))  # [1]
print(move_last_to_first([]))  # []
print(move_last_to_first([12, 3, 4, 10, 8]))  # [8, 12, 3, 4, 10]
