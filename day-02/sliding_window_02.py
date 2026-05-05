"""
Find the length of longest substring that contains at most two distinct characters
"""

def longest_substring_two_distinct(s):
    counts = {} # using dictionary to check for duplicates as well as count of chars
    left = 0
    max_length = 0
    for right in range(len(s)):  # right expands the window size
        char = s[right]
        counts[char] = counts.get(char, 0) + 1
        while len(counts) > 2: # contract the window if we have more than 2 distinct chars
            left_char = s[left]
            counts[left_char] -= 1
            if counts[left_char] == 0: # if count hits zero, remove it from dict entirely
                del counts[left_char]
            left += 1 # shrink the window
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_substring_two_distinct("ebbbccceaab"))