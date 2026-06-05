class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in strs:
            if len(i) < 1:
                strs[strs.index(i)] = 'X'

        encoded_string = "-".join(strs)

        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split('-')
        for i in decoded_strs:
            if i == 'X':
                decoded_strs[decoded_strs.index(i)] = ""
            elif len(i) < 1:
                return []
        
        return decoded_strs
