def bubble_sort(arr):
    # n = 0
    for i in range(0, len(arr), 1):
        has_swap = False
        for j in range(i + 1, len(arr), 1):
            # n = n + 1
            if arr[j] < arr[i]:
                value_j = arr[j]
                value_i = arr[i]
                arr[j] = value_i
                arr[i] = value_j
                has_swap = True

        if not has_swap:
            break

    # print('n = ', n)
    return arr


print('This is Selection Sort')
print('Worst Case still O(n^2)')
print('But Best Case is O(n)')
print('I have [3, 2, 5, 6, 7, 4, 1, 25]')
print('I will sort..., After sort The List is ', bubble_sort([3, 2, 5, 6, 7, 4, 1, 25]))

print('I have [1, 2, 7, 8, 9, 15, 20, 31, 32]')
print('I will sort..., After sort The List is ', bubble_sort([1, 2, 7, 8, 9, 15, 20, 31, 32]))
