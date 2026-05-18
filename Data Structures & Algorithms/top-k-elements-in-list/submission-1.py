class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        out = []

        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        sorted_arr = sorted(count.items(), key=lambda item: item[1])

        sorted_arr = sorted_arr[::-1]

        for i in range(0, k):
            out.append(sorted_arr[i][0])

        return out
