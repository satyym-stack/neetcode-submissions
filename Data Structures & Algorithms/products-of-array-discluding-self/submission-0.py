class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
                before = nums[:i]
                after = nums[i+1:]
                result.append(math.prod(before + after))

        return result