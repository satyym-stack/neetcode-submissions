class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    if len(seen) > max_length:
                        max_length = len(seen)
                else:
                    break

            seen = set()
        
        return max_length
