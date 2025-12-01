from typing import List
def task1ai(nums: List[int], target: int) -> List[int]:
    new_array=[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] - nums[j] == target:
                new_array = [i, j]

    return new_array