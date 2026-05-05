"""
Find the length of longest substring with no repeating characters
"""

def longest_unique_substring(s):
    left = 0
    substring = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left += 1
        substring.add(s[right])
        max_length = max(max_length, right  - left + 1)

    return max_length

print(longest_unique_substring("abbaecba"))