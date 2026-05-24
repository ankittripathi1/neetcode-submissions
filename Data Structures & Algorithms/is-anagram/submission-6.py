class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        str_dict =  {}

        for char in s:
            str_dict[char] = str_dict.get(char,0)+1

        for char in t:
            if char not in str_dict:
                return False
            str_dict[char] -= 1
            if str_dict[char] < 0:
                return False

        return True



