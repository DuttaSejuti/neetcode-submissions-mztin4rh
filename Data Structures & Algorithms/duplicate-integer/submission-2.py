class Solution:
    # TC: O(n) SC: O(n)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     return not len(set(nums)) == len(nums)
    

    # TC: O(n) SC: O(n)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     seen = set()
    #     for num in nums:
    #         if num not in seen:
    #             seen.add(num)
    #         else:    
    #             return True
    #     return False


    # TC: O(nlogn) SC: O(1)
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
