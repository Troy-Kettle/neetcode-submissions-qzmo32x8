class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) / 3
        d = defaultdict(int)

        out = []

        for i in nums:
            d[i] += 1

        for k, v in d.items():
            if v > n:
                out.append(k)

        return out



        