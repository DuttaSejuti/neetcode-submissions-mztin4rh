class Solution:
    # TC: O(n) SC: O(n)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     return not len(set(nums)) == len(nums)
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:    
                return True
        return False
