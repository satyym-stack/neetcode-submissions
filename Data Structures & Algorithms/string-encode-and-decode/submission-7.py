

class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for s in strs:
            encode_string += str(len(s)) + "#" + s
        return encode_string

    def decode(self, s: str) -> List[str]:
        decode_str = []
        i = 0
        while(i < len(s)):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            decode_str.append(s[i:j])
            i = j
        return decode_str

