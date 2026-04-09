class Solution:
    # TC:O(n) SC: O(n)
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     return nums + nums
    
    # TC:O(n) SC:O(1)
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums) # returns NONE; doesn't create a new list
        return nums
