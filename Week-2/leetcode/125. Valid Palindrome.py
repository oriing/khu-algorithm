class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_str = ""
        for i in s:
            if 'a' <= i <= 'z':
                s_str += i
            if 'A' <= i <= 'Z':
                s_str += i.lower()
            if '0' <= i <= '9':
                s_str += i
            
        for i in range(len(s_str)):
            if s_str[i] != s_str[-i-1]:
                return False
        
        return True
            