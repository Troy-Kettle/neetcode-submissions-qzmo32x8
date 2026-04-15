class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            groups[word_sorted].append(word)


        out = []

        for v in groups:
            out.append(groups[v])

        return out
