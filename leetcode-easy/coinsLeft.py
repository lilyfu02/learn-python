class Solution():
    def coins (self,n:int)-> int:
        i = 0
        turn = 0
        while n>i:
            i+=1
            n=n-i
            turn+=1
        return turn

solution = Solution()
print(solution.coins(8))

