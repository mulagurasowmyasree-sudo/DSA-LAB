def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

n=int(input("Enter the no of elements: "))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at position", result )
else:
    print("Element not found")
