class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
            new_min = min(nums[i], nums[i] * current_max, nums[i] * current_min)
            current_max = new_max
            current_min = new_min
            result = max(result, new_max)

        return result