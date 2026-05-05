# Sliding Window pattern (Same direction)

Use Case: Used for contiguous subarrays or substrings. Look for keywords like "longest", "smallest" or "subarray".

 - Logic:
  i. Expand the `right` pointer to grow the window.
  ii. Validate if the window still meets the problem's condition.
  iii. Contract the `left` pointer if the condition is broken (e.g., duplicate found).
 - Time Complexity: O(n) (Amortized - each element is visited at most twice).
 - Space Complexity: O(k) where k is the number of unique elements (stored in a `set` or `dict`).

##### Key Variants: 
 - Unique Substring: Use a `set()` to track if a character is already present.
 - K Distinct Characters: Use a `dict{char: count}` to track the frequency of chatacters.

#Crucial Delete the key from the dictionary when its count reaches zero.
#Note `counts.get(char, 0)` prevents any `KeyErrors` and `len(dict)` gives the count of keys in dictionary, which is it's length.