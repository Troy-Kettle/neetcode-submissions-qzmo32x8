class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(int)

        e = list(enumerate(nums))
        print(f'e = {e}')

        for i in e:
            if target - i[1] in seen:
                return([seen[target - i[1]], i[0]])
            else:
                seen[i[1]] = i[0]
                
        return
