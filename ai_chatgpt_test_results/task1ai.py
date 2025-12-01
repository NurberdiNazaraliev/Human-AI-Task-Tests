def task1ai(nums, target):
    seen = {}  
    for i, v in enumerate(nums):
        need = v - target
        if need in seen:
            return [i, seen[need]]
        seen[v] = i  

    return None
