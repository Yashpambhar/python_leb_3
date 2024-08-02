def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

elements = [1, 4, 2, 8, 23]
insertion_sort(elements)
print("Sorted elements:", elements)

output :-
![pro7](https://github.com/user-attachments/assets/a42f7b59-7122-4736-8d00-32aafe7dd0e8)
