# Runtime: 284 ms, faster than 19.63% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.8 MB, less than 61.65% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) // 2):
            result += nums[i * 2]
        return result

# 책의 솔루션
# Runtime: 272 ms, faster than 40.93% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.9 MB, less than 28.76% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])