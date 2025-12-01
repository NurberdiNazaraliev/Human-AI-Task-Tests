def task2(arr):
    sorted_list = arr[:]  
    for i in range(len(sorted_list)):
        min_pos = i
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_pos]:
                min_pos = j
        sorted_list[i], sorted_list[min_pos] = sorted_list[min_pos], sorted_list[i]
    return sorted_list