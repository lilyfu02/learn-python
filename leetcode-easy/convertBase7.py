class Solution:
    def baseSeven(self,num:int) -> str:
        remainders = []
        x = abs(num)
        if x==0:
            remainders = '0'
        else:
            while x>0:
                remainders.append(str(x%7))
                x //= 7
            remainders = ''.join(remainders[::-1])
            if num<0:
                remainders = '-'+remainders
        return remainders

solution = Solution()
n = input("num: ")
print(solution.baseSeven(int(n)))