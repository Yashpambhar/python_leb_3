def sequential_search(elements, search):
    for index, element in enumerate(elements):
        if element == search:
            return index
    return -1

elements = [1, 3, 5, 8, 10, 23, 35]
search_element = 10

result = sequential_search(elements, search_element)

if result != -1:
    print(f"Element {search_element} found at index {result}.")
else:
    print(f"Element {search_element} not found.")

output :-
![pro4](https://github.com/user-attachments/assets/ccc05b32-3f1c-4992-8fea-8907f2ec4415)
