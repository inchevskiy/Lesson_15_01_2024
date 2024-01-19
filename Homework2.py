number = int(input("Введіть чотиризначне число: "))

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

print(thousands)
print(hundreds)
print(tens)
print(ones)


