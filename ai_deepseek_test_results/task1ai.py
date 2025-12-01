def task1ai(nums, target):
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