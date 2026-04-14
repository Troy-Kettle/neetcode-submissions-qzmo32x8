class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def b_search(l,h,x):

            mid = l + (h - l) // 2

            if l > h:
                return -1

            if x > nums[mid]:
                return b_search(mid+1, h, x)
            elif x < nums[mid]:
                return b_search(l, mid-1, x)
            else:
                return mid

        return b_search(0, len(nums)-1, target)