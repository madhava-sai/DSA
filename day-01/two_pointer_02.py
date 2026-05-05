"""
Imagine a series of vertical lines drawn on a graph. The x-axis represents the index
and the height of the line at each index is given by an array of integers.
Find two lines that together with x-axis form a container that holds the most
water. Return the maximum area possible.
"""

def max_water(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0
    while left < right:
        width =  right - left
        height = min(arr[left], arr[right])
        area = width * height
        max_area = max(area, max_area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_water([1, 8, 6, 2, 5, 4]))