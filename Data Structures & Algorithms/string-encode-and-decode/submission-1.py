class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = str()
        for string in strs:
            string_len = len(string)
            encoded_string += f"{string_len}#{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0 
        while i< len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            words.append(word)
        
            i = j + 1 + length 
        return words

