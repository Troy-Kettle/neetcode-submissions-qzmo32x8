class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d = defaultdict(int)

        for i in nums:
            if d[i] < 1:
                d[i] += 1
            else:
                return True

        return False

        

