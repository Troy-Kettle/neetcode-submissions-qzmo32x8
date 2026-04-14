from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        first = []
        second = []

        for i in s:
            first.append(i)

        for i in t:
            second.append(i)

        first.sort()
        second.sort()

        if first == second:
            return True
        else:
            return False

