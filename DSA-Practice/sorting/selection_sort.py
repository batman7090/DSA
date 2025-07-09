def selection_sort(arr):
    for i in range(len(arr)):
        curr_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                curr_min = j
        arr[i], arr[curr_min] = arr[curr_min], arr[i] 
    return arr

a = [2, 6, 5, 1, 3, 4]

print(selection_sort(a))
