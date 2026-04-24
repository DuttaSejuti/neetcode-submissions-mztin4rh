class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        multi = 1
        result = [0]*len(nums)

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                multi *= num
        
        if zero_count > 1:
            return result
        
        for i in range(len(nums)):
            # element itself is zero
            if nums[i] == 0:
                if zero_count == 1:
                    result[i] = multi
            else:
                if zero_count == 1:
                    result[i] = 0
                else:
                    result[i] = multi // nums[i]
        
        return result
