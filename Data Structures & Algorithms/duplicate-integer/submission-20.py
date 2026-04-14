class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = []

        x = range(len(nums))

        for i in x:
            if nums[i] in seen:
                return True
            else:
                seen.append(nums[i])
                i += 1


        return False