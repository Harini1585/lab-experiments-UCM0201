
print("BINARY SEARCH COST ANALYSIS")
print("----------------------------")

# 1. Accept number of elements
n = int(input("Enter the number of elements: "))

# 2. Create a sorted list
arr = list(range(1, n + 1))

target = int(input("Enter the element to search: "))

# 3. Implement binary search and count comparisons
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

# 4. Perform binary search
position, comparisons = binary_search(arr, target)

# 5. Display results
if position != -1:
    print("\nElement found at position:", position + 1)
else:
    print("\nElement not found.")

print("Number of comparisons:", comparisons)
