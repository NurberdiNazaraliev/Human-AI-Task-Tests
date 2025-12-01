def task1(nums, target):
    seen = {} 

    for i, v in enumerate(nums):
        need = target - v
        if need in seen:  
            return [seen[need], i]
        seen[v] = i          

    return None
