class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charS, charT = {}, {}
        is_valid = True
        best_i, best_j = 0, 0
        min_length = float('inf')
        if t == "":
            return ""
        
        for i in t:
            charT[i] = charT.get(i, 0) + 1
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                charS[s[j]] = charS.get(s[j], 0) + 1
                for c in charT:
                    if charS.get(c,0) < charT[c]:
                        is_valid = False
                        break
                if is_valid:
                    window_length = j - i + 1
                    if window_length < min_length:
                        min_length = window_length
                        best_i = i
                        best_j = j
                is_valid = True
            charS = {}

        if min_length == float('inf'):
            return ""    
        return s[best_i: best_j+1]
