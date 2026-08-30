class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        longest_palindrome = 0
        for i in range(len(s)):
            odd_length = expansion(i, i)
            even_length = expansion(i, i + 1)
            current_longest = max(odd_length, even_length)
            if current_longest > longest_palindrome:
                longest_palindrome = current_longest
                start = i - ((current_longest - 1) // 2)
                end = i + ((current_longest) // 2)
    
        return s[start :end + 1]

            

