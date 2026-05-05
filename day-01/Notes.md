# Two-pointer pattern (Opposite ends)

 Use case: Often used on sorted arrays to find pairs, or for "containers" where we ned to maximize/minimize a value by comparing elements from both ends.

 - Logic: Initialize `left = 0` and `right = len(arr) - 1`. Move towards each other based on a condition.
 - Time Complexity: O(n)
 - Space Complexity: O(1)
 - Key problem: Container with Most Water.
    i. Decision Rule: Move the pointer pointing to the shorter wall to find a potentially taller one.