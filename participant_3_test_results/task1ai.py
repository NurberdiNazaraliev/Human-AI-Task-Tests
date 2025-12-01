from typing import List
def task1ai(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, num in enumerate(nums):
        complement1 = num - target
        complement2 = num + target

        if complement1 in lookup:
            return [i, lookup[complement1]]
        if complement2 in lookup:
            return [lookup[complement2], i]

        lookup[num] = i
