class Solution():
    def palindrome(self, x: int) -> bool:
        orig = x
        value = 0
        if x < 0:
            return False
        else:
            while x != 0:
                value = value * 10 + x % 10
                x //= 10

        return value == orig


solution = Solution()
ques = input("the number: ")
print(solution.palindrome(int(ques)))
