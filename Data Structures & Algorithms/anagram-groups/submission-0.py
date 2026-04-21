class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)

        for s in strs:
            temp = "".join(sorted(s))
            result_map[temp].append(s)
        
        return list(result_map.values())