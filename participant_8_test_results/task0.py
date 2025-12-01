def task0(nums):
    count = 0
    for x in nums:
        if not x % 2:
            count += 1
    return count
