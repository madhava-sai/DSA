"""
Check if a string is palindrome
"""

def string_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            # Moving the pointers towards each other since the characters matched.
            left += 1
            right -= 1
        else:
            return "Not Palindrome"
    return  "Palindrome"

print(string_palindrome("abba"))