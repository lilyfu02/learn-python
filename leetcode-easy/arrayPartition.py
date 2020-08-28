from typing import List


class Solution:
    @staticmethod
    def array_pa(nums: List[int]) -> int:
        nums = sorted(nums)
        n = int((len(nums)) / 2)
        sum = 0

        for i in range(0, (n + 2), 2):
            sum += min(nums[i], nums[i + 1])
        return sum


num = [1, 2, 4, 3, 5, 8]
solution = Solution()
print(solution.array_pa(num))
