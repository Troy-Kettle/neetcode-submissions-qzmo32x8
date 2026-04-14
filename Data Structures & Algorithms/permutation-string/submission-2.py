class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)

        s1.sort()

        w = len(s1)

        for i in range (len(s2)):
            temp = []
            for i in s2[i:i+w]:
                temp.append(i)
            temp.sort()

            if temp == s1:
                return True

        return False
            