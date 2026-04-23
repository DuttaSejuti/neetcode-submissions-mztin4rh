class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            l = len(s)
            result.append(f"{l}#{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        result = []
        start = 0
        "5#hello5#world"
        while start < len(s):
            hash_idx = s.find('#', start)
            str_len = int(s[start:hash_idx])
            start = hash_idx + 1
            temp = s[start:start+str_len]
            result.append(temp)
            start += str_len
        
        return result
