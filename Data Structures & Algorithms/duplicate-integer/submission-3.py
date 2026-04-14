class Solution:
    from collections import defaultdict
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = defaultdict(list)
        
        
        for num in nums:
            if seen[num] == num:
                return True
            else:
                seen[num] = num

        return False

         