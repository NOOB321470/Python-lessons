def binary_search_recursion(data, target):
    if data == []:
        return False
    elif len(data) == 1:
        return data[0] == target
    else:
        half = len(data) // 2
        if data[half] > target:
            return binary_search_recursion(data[:half], target)
        else:
            return binary_search_recursion(data[half:], target)
print(binary_search_recursion([1, 2, 3, 4, 5, 6], 52))