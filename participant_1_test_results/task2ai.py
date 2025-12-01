def task2ai(a):
    def insertion(lo, hi):
        for i in range(lo + 1, hi + 1):
            key = a[i]
            j = i - 1
            while j >= lo and a[j] < key: 
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    def median_of_three(i, j, k):
        x, y, z = a[i], a[j], a[k]
        if x < y:
            if y < z: return j
            return i if x > z else k
        else:
            if x < z: return i
            return j if y > z else k

    def sort(lo, hi):
        while lo < hi:
            if hi - lo < 16: 
                insertion(lo, hi)
                return
            m = (lo + hi) // 2
            piv_idx = median_of_three(lo, m, hi)
            a[lo], a[piv_idx] = a[piv_idx], a[lo]
            p = a[lo]

        
            lt, i, gt = lo, lo + 1, hi
            while i <= gt:
                if a[i] > p:
                    a[lt], a[i] = a[i], a[lt]
                    lt += 1; i += 1
                elif a[i] < p:
                    a[i], a[gt] = a[gt], a[i]
                    gt -= 1
                else:
                    i += 1

            if (lt - lo) < (hi - gt):
                sort(lo, lt - 1)
                lo = gt + 1
            else:
                sort(gt + 1, hi)
                hi = lt - 1

    sort(0, len(a) - 1)
    return a