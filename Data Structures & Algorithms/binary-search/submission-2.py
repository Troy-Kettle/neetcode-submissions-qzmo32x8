class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def b_search(nums, target, l, h):

            mid = l + (h - l) // 2

            if l > h:
                return -1
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return b_search(nums, target, mid+1, h)
            elif target < nums[mid]:
                return b_search(nums, target, l, mid-1)
        
        l = 0
        h = len(nums) - 1
        return b_search(nums, target, l, h)
