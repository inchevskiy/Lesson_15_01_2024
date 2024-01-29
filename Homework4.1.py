def move_zeros(lst):
  non_zeros = []

  zeros_count = 0

  for x in lst:

    if x != 0:
      non_zeros.append(x)

    else:
      zeros_count += 1

  non_zeros.extend([0] * zeros_count)

  return non_zeros


print(move_zeros([0, 1, 0, 12, 3]))
print(move_zeros([0]))
print(move_zeros([1, 0, 13, 0, 0, 0, 5]))
print(move_zeros([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))