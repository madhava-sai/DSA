"""
Find the length of longest substring with no repeating characters
"""

def longest_unique_substring(s):
    left = 0
    substring = set() # using set to check for duplicates
    max_length = 0

    for right in range(len(s)): # right expands the window size
        while s[right] in substring: # if we hit a duplicate we shrink from the left
            substring.remove(s[left])
            left += 1
        substring.add(s[right]) # here we are sure that window is unique, add the new char
        max_length = max(max_length, right  - left + 1) # update global maximum. (right - left + 1) gives us the current window size

    return max_length

print(longest_unique_substring("abbaecba"))