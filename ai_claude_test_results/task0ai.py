def task0ai(numbers):
    odd_nums = []
    for num in numbers:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums