def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:1
            return mid

    # If we reach here, then the element was not present
    return -1

x = int(input("enter value to find"))

arr  = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,110]
print(binary_search(arr,x))