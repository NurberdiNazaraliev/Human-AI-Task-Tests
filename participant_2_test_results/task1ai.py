from typing import List

def task1ai(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):

        complement1 = nums[i] - target
        if complement1 in hashmap:
            return [i, hashmap[complement1]]

        complement2 = nums[i] + target
        if complement2 in hashmap:
            return [hashmap[complement2], i]
        
        hashmap[nums[i]] = i
    return []
