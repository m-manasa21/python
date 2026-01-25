class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_linear(arr):
            prev1 = 0
            prev2 = 0
            for n in arr:
                curr = max(prev1, prev2 + n)
                prev2 = prev1
                prev1 = curr
            return prev1
        money1 = rob_linear(nums[:-1])
        money2 = rob_linear(nums[1:])
        return max(money1, money2)
