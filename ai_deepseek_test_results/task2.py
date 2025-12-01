
def task2(arr):
    """Sort list in increasing order using selection sort"""
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr