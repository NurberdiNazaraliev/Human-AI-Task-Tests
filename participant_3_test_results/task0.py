def task0(numbers):
    count_even = sum(1 for n in numbers if n % 2 == 0)
    return count_even
