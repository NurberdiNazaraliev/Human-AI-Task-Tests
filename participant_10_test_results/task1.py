from typing import List
def task1(nums: List[int], target: int) -> List[int]:
    new_array=[]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                new_array = [i, j]
    return new_array