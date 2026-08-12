def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
n = int(input("Enter number of elements: "))
arr = []
print("Enter", n, "elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

result = binary_search(arr, key)

if result != -1:
    print("Element found at position", result + 1)
else:
    print("Element not found")
