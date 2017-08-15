def selection_sort(arr):
    len_of_arr = len(arr)
    for i in range(0, len_of_arr, 1):
        current_arr = arr[i]

        min_arr = arr[i]
        index_of_min = i
        for j in range(i + 1, len_of_arr, 1):
            if arr[j] < min_arr:
                index_of_min = j
                min_arr = arr[j]

        arr[i] = min_arr
        arr[index_of_min] = current_arr

    return arr


print('This is Selection Sort')
print('Worst Case is O(n^2)')
print('I have [3, 2, 5, 6, 7, 4, 1, 25]')
print('I will sort..., After sort The List is ', selection_sort([3, 2, 5, 6, 7, 4, 1, 25]))
