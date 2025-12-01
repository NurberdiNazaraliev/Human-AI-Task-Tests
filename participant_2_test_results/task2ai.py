def task2ai(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count) - 1, -1, -1):  
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr
