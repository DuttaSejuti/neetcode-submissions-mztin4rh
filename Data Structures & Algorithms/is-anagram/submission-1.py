class Solution:
    # TC: O(nlogn) SC: O(n)
    # sorted(s) => TC:O(nlogn) SC:O(n)
    # comparison TC: O(n)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0]*26
        count_t = [0]*26
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1
        
        return count_s == count_t
