def sequential_search(arr, search_key):
    len_of_arr = len(arr)
    for i in range(0, len_of_arr, 1):
        if search_key == arr[i]:
            return True

    return False

print('This is Sequential Search')
print('Worst Case is O(n)')
print('I have [3, 2, 5, 6, 7, 4, 1, 25]')
print('Has 2 ? ', sequential_search([3, 2, 5, 6, 7, 4, 1, 25], 5))
print('Has 62 ? ', sequential_search([3, 2, 5, 6, 7, 4, 1, 25], 62))
