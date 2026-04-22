class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        result = []
        # O(n)
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        # O(nlogn)
        value_sort = sorted(freq_map.values(), reverse=True)[:k]
        
        # O(n*k)
        for key, v in freq_map.items():
            if v in value_sort:
                result.append(key)

        return result 
