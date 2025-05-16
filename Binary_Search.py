def binary_search(a, n):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == n:
            return True  
        elif a[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    return False


a = [2, 4, 7, 10, 15, 20, 25]
n = 20

result = binary_search(a, n)
print("Element found in the array.", n)
