from typing import List

def task1ai(nums: List[int], target: int) -> List[int]:
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i != j and a - b == target:
                return [i, j]
    return []
