class Solution:
    # TC: O(m*nlogn) SC: O(m*n)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result_map = defaultdict(list)

    #     for s in strs:
    #         temp = "".join(sorted(s))
    #         result_map[temp].append(s)
        
    #     return list(result_map.values())

    # TC: O(m*n) SC: O(m*n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(s)

        return list(result.values())
