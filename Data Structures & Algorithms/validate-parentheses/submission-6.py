class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if "()" in s:
                s = s.replace("()", (""))
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            
            if len(s) == 0:
                return True
    
        return False