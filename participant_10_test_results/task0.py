def task0(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count