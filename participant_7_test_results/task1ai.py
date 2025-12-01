from typing import List
def task1ai(nums: List[int], target: int)-> List[int]:
    output=[]
    for i in range (0, len(nums)):
        for j in range (0, len(nums)):
            if i!=j and nums[i]-nums[j]==target:
                output=[i,j]

            
    return output