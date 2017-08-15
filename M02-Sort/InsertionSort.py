def insertion_sort(arr):
    # n = 0
    for i in range(0, len(arr), 1):
        value_index_i = arr[i]
        hole = i

        while hole > 0 and arr[hole - 1] > value_index_i:
            arr[hole] = arr[hole - 1]
            hole = hole - 1

        arr[hole] = value_index_i
    # print('n = ', n)
    return arr


print('This is Insertion Sort')
print('Worst Case still O(n^2)')
print('But Best Case is O(n)')
print('I have [3, 2, 5, 6, 7, 4, 1, 25]')
print('I will sort..., After sort The List is ', insertion_sort([3, 2, 5, 6, 7, 4, 1, 25]))

print('I have [1, 2, 7, 8, 9, 15, 20, 31, 32]')
print('I will sort..., After sort The List is ', insertion_sort([1, 2, 7, 8, 9, 15, 20, 31, 32]))
