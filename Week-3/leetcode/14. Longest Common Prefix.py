class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for i in range(min(map(len, strs))):
            now = strs[0][i]
            for s in strs:
                if now != s[i]:
                    return prefix
            prefix += now
        return prefix