def merge(arr, low, mid, high):
    # overall array will divided into 2 array
    # left_arr contains the left portion of array from left to mid
    # right_arr contains the right portion of array from mid + 1 to right
    left_arr = arr[low : mid + 1]
    right_arr = arr[mid + 1 : high + 1]
    k = low
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        # change sign for Descending order
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr


def mergesort(arr, low, high):
    """
    >>> mergesort([3, 2, 1], 0, 2)
    [1, 2, 3]
    >>> mergesort([3, 2, 1, 0, 1, 2, 3, 5, 4], 0, 8)
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    """
    if low < high:
        mid = (low + high) // 2
        # print("ms1",a,b,m)
        mergesort(arr, low, mid)
        # print("ms2",a,m+1,e)
        mergesort(arr, mid + 1, high)
        # print("m",a,b,m,e)
        merge(arr, low, mid, high)
        return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
