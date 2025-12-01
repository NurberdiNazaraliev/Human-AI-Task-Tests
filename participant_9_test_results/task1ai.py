from typing import List

def task1ai(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for j, value in enumerate(nums):
        need = value + target   
        if need in lookup:
            return [lookup[need], j]
        lookup[value] = j
    return []
