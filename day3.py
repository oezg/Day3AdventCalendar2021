import numpy as np

with open("day3_input") as inp:
    numbers = inp.readlines()

numbers = [number.rstrip() for number in numbers]
numbers = [list(number) for number in numbers]
numbers = [[int(num) for num in row] for row in numbers]
nums = np.array(numbers)
gamma = np.median(nums, axis=0)
gamma_list = [int(g) for g in list(gamma)]
epsilon_list = [0 if g == 1 else 1 for g in gamma_list]
digit_factor = 1
gamma_decimal = 0
for digit in gamma_list[::-1]:
    gamma_decimal += digit * digit_factor
    digit_factor *= 2
digit_factor = 1
epsilon_decimal = 0
for digit in epsilon_list[::-1]:
    epsilon_decimal += digit * digit_factor
    digit_factor *= 2
print(epsilon_decimal * gamma_decimal)