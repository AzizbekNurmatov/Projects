def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Print the list after each pass
        print(f"Pass {i+1}: {arr}")

    return arr

# Example list
example_list = [64, 25, 12, 22, 11]

# Sorting the list
sorted_list = selection_sort(example_list)

print("Final Sorted list:", sorted_list)
