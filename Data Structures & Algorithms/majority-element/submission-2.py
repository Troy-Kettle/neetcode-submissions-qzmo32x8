class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        most_common = sorted(d.items(), key=lambda item: item[1])

        return most_common[-1][0]