from math import ceil, floor
import numpy as np


with open("day3_input") as inp:
    numbers = [n.rstrip() for n in inp.readlines()]


def rating(nums, co2=False):
    length = len(nums[0])
    for i in range(length):
        digits = np.array([int(num[i]) for num in nums])
        common = ceil(np.median(digits))
        if co2:
            common = 0 if common else 1
        nums = list(filter(lambda num: int(num[i]) == common, nums))
        if len(nums) == 1:
            rate = int(nums[0], 2)
            return rate
    return 0

oxygen = rating(numbers.copy())
carbon = rating(numbers.copy(), True)
print("life_support = ", oxygen * carbon)