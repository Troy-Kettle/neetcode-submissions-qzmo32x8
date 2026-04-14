class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = [x for x in s]
        t1 = [x for x in t]

        s1.sort()
        t1.sort()

        if s1 == t1:
            return True
        else:
            return False