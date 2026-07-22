class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for ch in s:
            if ch.isalnum():
                s1 = s1 + ch.lower()

        P = ""
        for i in range(len(s1) - 1, -1, -1):
            if s1[i].isalnum():
                P = P + s1[i]
        if s1 == P:
            return True
        return False