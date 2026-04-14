class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        max_element = []

        for i in range(len(nums) - k + 1):

            current_sum = max(nums[i:i+k])
            max_element.append(current_sum)

        return max_element