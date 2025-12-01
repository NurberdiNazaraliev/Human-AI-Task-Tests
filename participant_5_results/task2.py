def task2(lst):
    length = len(lst)
    for pass_num in range(length-1, 0, -1):
        for i in range(pass_num):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst