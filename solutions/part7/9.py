import collections
import copy

# set으로 보낼 시
# Runtime: 9588 ms, faster than 5.01% of Python3 online submissions for 3Sum.
# Memory Usage: 17.7 MB, less than 39.58% of Python3 online submissions for 3Sum.
# list로 변환 시
# Runtime: 9460 ms, faster than 5.01% of Python3 online submissions for 3Sum.
# Memory Usage: 19 MB, less than 10.18% of Python3 online submissions for 3Sum.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        if len(nums) < 3:
            return []

        result = set()

        count = collections.Counter(nums)
        count_keys = list(count.keys())
        count_keys.sort()

        for i, v in enumerate(count_keys):
            count2 = copy.deepcopy(count)
            left = i
            right = len(count_keys) - 1
            count2[v] -= 1
            if count2[v] == 0:
                left += 1
            while left < right:
                left_val = count_keys[left]
                right_val = count_keys[right]

                if left_val + right_val + v == 0:
                    result.add((v, left_val, right_val))
                    right -= 1
                    left += 1
                elif left_val + right_val + v > 0:
                    right -= 1
                else:
                    left += 1

            if left == right and count2[count_keys[left]] > 1 and (2 * count_keys[left]) + v == 0:
                left_val = count_keys[left]
                result.add((v, left_val, left_val))

        # result = [list(v) for v in result]
        return result

# Runtime: 940 ms, faster than 57.79% of Python3 online submissions for 3Sum.
# Memory Usage: 17.4 MB, less than 87.04% of Python3 online submissions for 3Sum.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        result = []

        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                left_value = nums[left]
                right_value = nums[right]
                sum_value = v + left_value + right_value

                if sum_value == 0:
                    temp = [v, left_value, right_value]
                    if len(result) > 0 and result[-1] != temp:
                        result.append([v, left_value, right_value])
                    elif len(result) == 0:
                        result.append([v, left_value, right_value])
                    while left > right and sums[left] == sums[left + 1]:
                        left += 1
                    while left > right and sums[right] == sums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1

                elif sum_value > 0:
                    right -= 1

                else:
                    left += 1
        return result


# 책의 솔루션

# Runtime: 804 ms, faster than 77.35% of Python3 online submissions for 3Sum.
# Memory Usage: 17.5 MB, less than 51.63% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        result = []

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val < 0:
                    left += 1
                elif sum_val > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result



