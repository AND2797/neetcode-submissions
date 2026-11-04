class Solution:
    """
    Time: O(n)
    Space: O(n)
    Left to right compute:
    res[i] = prefix (because this is the value computed from numbers seen before)

    Right to left compute:
    res[i] *= postfix (we have to multiply with the value computed from the left to right computation above)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res



        