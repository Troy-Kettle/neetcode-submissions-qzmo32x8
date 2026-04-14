class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []

        for i in list(s.lower()):
            if i.isalnum():
                s1 += i

        return s1 == s1[::-1]
        
