def binary_search(arr, search_key):
    len_of_arr = len(arr)
    left = 0
    right = len_of_arr - 1

    while left <= right:
        mid = (right + left) // 2
        # print('left ', left, '\tright ', right, '\tmid ', mid)
        if search_key == arr[mid]:
            return True
        elif search_key > arr[mid]:
            left = mid + 1
        elif search_key < arr[mid]:
            right = mid - 1

    return False


print('This is Binary Search. I\' do search better than sequential search but my list must ordered')
print('Worst Case is O(log n)')
print('I have [1, 2, 3, 4, 5, 6, 7, 25]')
print('Has 3 ? ', binary_search([1, 2, 3, 4, 5, 6, 7, 25], 3))
print('Has 8 ? ', binary_search([1, 2, 3, 4, 5, 6, 7, 25], 8))
