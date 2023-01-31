######################################
# Quick Sort Algorithms(Iterative) taken from:
# url: https://www.geeksforgeeks.org/iterative-quick-sort/
# on 01/28/2023
# Author: Mohit Kumra
# License: Share-alike
# url: https://www.geeksforgeeks.org/copyright-information/?ref=footer#
# Selection Sort Algorithms(Iterative) taken from:
# url: https://www.geeksforgeeks.org/selection-sort/
# on 01/27/2023
# License: Share-alike
# url: https://www.geeksforgeeks.org/copyright-information/?ref=footer
# Changelog:
# - add a compare function to Quick sort and Selection sort
######################################


def partition(arr, l, h, compare):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if compare(arr[j], x):
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(arr, l, h, compare):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h, compare)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h



# This code is contributed by Mohit Kumra


def selection_sort(array, compare):
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(array)):
            if compare(array[min_idx], array[j]):
                min_idx = j
        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]


# end def selection_sort(array):


if __name__ == "__main__":
    # Drive code to test above
    print("Sorted array")
    px1 = ((255, 32, 12), (0, 10))
    px2 = ((128, 255, 255), (20, 30))
    px3 = ((128, 255, 255), (20, 30))
    px4 = ((28, 255, 255), (20, 30))
    px5 = ((18, 255, 255), (20, 30))

    pxls = [px1, px2, px3, px4, px5]

    n = len(pxls)

    quickSortIterative(pxls, 0, n - 1)
    print("Sorted array is:")
    print(pxls)
