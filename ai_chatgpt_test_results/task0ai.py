def get_odds(numbers):
    odds = []
    for n in numbers:
        if n % 2 != 0:
            odds.append(n)
    return odds

