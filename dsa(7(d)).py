def linearSearch(list1, n, x):
    for i in range(0, n):
        if (list1[i] == x):
            return i
    return -1
list1 = [2, 4, 0, 1, 9]
x = int(input("Enter the element to search:"))
n = len(list1)
result = linearSearch(list1, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
