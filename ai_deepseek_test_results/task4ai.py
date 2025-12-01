def task4ai(num):
    if not isinstance(num, int) or num < 1 or num > 3999:
        raise ValueError("Input must be an integer between 1 and 3999")
    
    val_to_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    roman_str = ''
    
    for value, symbol in val_to_roman:
 
        while num >= value:
            roman_str += symbol
            num -= value
    
    return roman_str