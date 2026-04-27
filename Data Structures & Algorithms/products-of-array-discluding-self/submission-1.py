class Solution:
    # 1, 1, 2, 8 -> nums left to right (1, n); result[i] = nums[i-1]*result[i]
    # 48,24,12,8 -> nums right to left (n-2, -1);result[i] = result[i]*nums[i+1]

    # TC: O(n), SC:O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        left_prod, right_prod = 1, 1

        for i in range(1, n):
            left_prod *= nums[i-1]
            result[i] = result[i] * left_prod
        
        for i in range(n-2, -1, -1):
            right_prod *= nums[i+1]
            result[i] = result[i] * right_prod
        
        return result

        
    # with division => TC: O(n), SC: O(n)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     zero_count = 0
    #     multi = 1
    #     result = [0]*len(nums)

    #     for num in nums:
    #         if num == 0:
    #             zero_count += 1
    #         else:
    #             multi *= num

    #     # if there are more than 1 zero, the whole result will be array of zero
    #     if zero_count > 1:
    #         return result
        
    #     for i in range(len(nums)):
    #         # element itself is zero
    #         if nums[i] == 0:
    #             # the element is the single zero in the array
    #             if zero_count == 1:
    #                 result[i] = multi
    #         else:
    #             if zero_count == 1:
    #                 result[i] = 0
    #             else:
    #                 result[i] = multi // nums[i]
        
    #     return result
