from typing import List
def task1ai(nums: List[int], target: int)-> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] - nums[j] == target:
                result=[i, j]
    return result