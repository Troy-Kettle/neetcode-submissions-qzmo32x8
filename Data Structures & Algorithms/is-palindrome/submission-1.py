class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []

        for i in list(s):
            if i.isalnum():
                s1.append(i.lower())

        return s1 == s1[::-1]

