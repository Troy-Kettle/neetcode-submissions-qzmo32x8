class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()

        s = list(s)
        t = list(t)

        s.sort()
        t.sort()
        
        if s == t:
            return True
        else:
            return False