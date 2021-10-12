data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = int(input("Enter your target: "))

# Linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target :
            return i
    return False

# Iterative Binary search
# To build a binary search your data must be sorted first - in this code we sorted it in Ascending order.
def binary_search_iterative(data, target):
    low = 0                   # as an index of first item
    high = len(data) - 1      # as an index of last item

    while low <= high :

        mid = (low + high) // 2   # as an index of middle item
        guess = data[mid]

        if guess == target :
            return mid
        elif guess < target :
            low = mid + 1
        else :
            high = mid - 1

    return False

#linear_search(data, target)
binary_search_iterative(data, target)