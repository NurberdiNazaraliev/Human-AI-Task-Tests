def main():
    # Task 1: Count even numbers
    numbers = [1, 6, 3, 4, 11, 6, 9, 8, 9, 10]
    even_count = len([num for num in numbers if num % 2 == 0])
    print(f"Even numbers count: {even_count}")
    
    # Task 2: Get odd numbers
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(f"Odd numbers: {odd_numbers}")
    
    # Task 3: Two Sum (Addition)
    def two_sum_add(nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
    
    # Task 4: Two Numbers (Subtraction)
    def two_numbers_subtract(nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement1 = num - target
            if complement1 in num_dict:
                return [i, num_dict[complement1]]
            
            complement2 = num + target
            if complement2 in num_dict:
                return [i, num_dict[complement2]]
            
            num_dict[num] = i
        return []
    
    # Test Two Sum (Addition)
    test_cases_add = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]
    
    print("\nTwo Sum (Addition) Results:")
    for nums, target in test_cases_add:
        result = two_sum_add(nums, target)
        print(f"nums={nums}, target={target} -> {result}")
    
    # Test Two Numbers (Subtraction)
    test_cases_sub = [
        ([2, 7, 11, 15], 13),
        ([3, 2, 4], -1),
        ([3, 3], 0)
    ]
    
    print("\nTwo Numbers (Subtraction) Results:")
    for nums, target in test_cases_sub:
        result = two_numbers_subtract(nums, target)
        print(f"nums={nums}, target={target} -> {result}")

if __name__ == "__main__":
    main()