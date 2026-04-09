class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, 1
        result = list()
        ele_map = defaultdict(list) # {0: [], ...}

        for idx, num in enumerate(nums):
            ele_map[num].append(idx) # { 3: [0], 4:[1], 5:[2], 6:[3]} or {5:[0,1]} 5:[0]

        for k, v in ele_map.items():
            rest = target - k
            if rest in ele_map:
                rest_ids = ele_map[rest]
                if rest == k:
                    if len(rest_ids) > 1:
                        return rest_ids[:2]
                else:
                    return[v[0], rest_ids[0]]
        