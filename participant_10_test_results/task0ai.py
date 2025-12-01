def task0ai(numbers):
    odd_numbers = []

    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    
    return odd_numbers