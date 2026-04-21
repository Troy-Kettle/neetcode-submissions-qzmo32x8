class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums

        ans = []
        for i in nums:
            ans.append(i)
        
        for i in nums2:
            ans.append(i)
       
        return ans

