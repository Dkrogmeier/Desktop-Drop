#Binary Search

def BS(arr, x):
    left = 0
    right = len(arr)-1
    while (left <= right):
        mid = left + right // 2
        if arr[mid] == x:
            return True
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid - 1
    return False

arr = [1, 2, 4, 5, 6, 7]
x = 5
BS(arr, x)

result = BS(arr, x)
print(result)

