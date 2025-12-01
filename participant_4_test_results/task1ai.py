from typing import List

def task1ai(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement1 = target + num  
        complement2 = num - target  
        
        if complement1 in num_map:
            return [num_map[complement1], i]  
        if complement2 in num_map:
            return [i, num_map[complement2]]  
        
        num_map[num] = i
    return []