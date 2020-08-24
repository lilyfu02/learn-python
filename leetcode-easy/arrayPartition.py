class Solution():
    def arrayPa (self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = int((len(nums)) - 1)
        sum = 0

        for i in range(0, n, 2):
            sum += min(nums[i], nums[i + 1])
        return sum



