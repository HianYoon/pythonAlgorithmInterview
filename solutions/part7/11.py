# if using division
# Runtime: 228 ms, faster than 90.03% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21 MB, less than 82.49% of Python3 online submissions for Product of Array Except Self.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for i in nums:
            if i == 0 and count_zero > 1:
                return [0] * len(nums)
            elif i == 0 and count_zero == 0:
                count_zero += 1
                continue
            product *= i
        for i, v in enumerate(nums):
            if v != 0 and count_zero == 0:
                nums[i] = product // v
            elif v != 0 and count_zero == 1:
                nums[i] = 0
            else:
                nums[i] = product
        return nums

