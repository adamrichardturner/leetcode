class Solution:
    """
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
    causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    Example 1:

    Input: x = 123
    Output: 321
    """
    def reverse(x: int) -> int:
        return int(''.join([char for char in str(x)[::-1]]))

print(Solution.reverse(123)) # 321