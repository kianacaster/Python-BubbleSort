def bubblesort(arr): # Define a function that takes an array to sort as a parameter
    for i in range(len(arr)): # Loop over the array to make sure the array is sorted
        for j in range(len(arr) - 1): # A nested loop where all the sorting happens
            if arr[j] > arr[j + 1]: # If the current index is larger than the one infront...
                temp = arr[j + 1] # Temporarily store the smaller value
                arr[j + 1] = arr[j] # Set the index at [j + 1] to be the one at [j]
                arr[j] = temp # Since the value at [j] has been overriden, use the temporary variable to change that value
    return arr # Return the sorted array                
