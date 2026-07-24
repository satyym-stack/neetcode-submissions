class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l = 0
       max_size = 0
       charSet = set()
       for r in range(len(s)):
            while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            window_size = r - l + 1
            max_size = max(max_size, window_size)
    
       return max_size

