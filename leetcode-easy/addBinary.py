class Solution():
    def addBinary (self, num1:str,num2:str) -> str:
        final = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(0,len(num1)):
            if num1[i] == '1':
                final += 2**i

        for i in range(0,len(num2)):
            if num2[i] == '1':
                final += 2**i
        total = str("{:b}".format(final))
        return total


solution = Solution()
first = input("first: ")
second = input("second: ")
print(solution.addBinary(first,second))