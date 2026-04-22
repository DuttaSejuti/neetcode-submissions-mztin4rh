class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq_map = dict()
    #     result = []
    #     # O(n)
    #     for n in nums:
    #         freq_map[n] = freq_map.get(n, 0) + 1
        
    #     # O(nlogn)
    #     value_sort = sorted(freq_map.values(), reverse=True)[:k]
    #     value_set = set(value_sort)
        
    #     # O(n)
    #     for key, v in freq_map.items():
    #         if v in value_set: # O(1)
    #             result.append(key)

    #     return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        result = []
        # O(n)
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        heap = [] # min-heap
        # m = no of unique elements in nums; keys in the map
        # k = size of the heap, as the size is not bigger than k
        # O(m*logk)
        for key in freq_map.keys():
            heapq.heappush(heap, (freq_map[key], key)) # log(k)
            # after popping the smallest everytime, heap will contain the max k
            if len(heap) > k:
                heapq.heappop(heap) # log(k)
        
        # O(klogk)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
        

