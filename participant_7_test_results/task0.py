from typing import List
def task0(nums: List[int]):
    even=0
    for i in nums:
        if i%2==0:
            even+=1
    return even
    