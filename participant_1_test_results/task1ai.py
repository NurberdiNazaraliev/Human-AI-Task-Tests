from typing import List
def task1ai(nums: List[int], target: int) -> List[int]:
    seen = {}  
    for i, v in enumerate(nums):
        need = v - target  
        if need in seen:
            return [i, seen[need]]  
        seen[v] = i
    return [] 