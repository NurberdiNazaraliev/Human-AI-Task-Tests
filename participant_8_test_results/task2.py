def task2(arr):
    res = list(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(res) - 1):
            if res[i] > res[i+1]:
                res[i], res[i+1] = res[i+1], res[i]
                swapped = True
    return res
