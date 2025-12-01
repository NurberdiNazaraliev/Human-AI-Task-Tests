def task2ai(arr):
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] > sorted_arr[max_idx]:
                max_idx = j
        sorted_arr[i], sorted_arr[max_idx] = sorted_arr[max_idx], sorted_arr[i]
    return sorted_arr