
class Solution(object):
    def reverse(self,x):
        larRange = (pow(2,31))-1
        smaRange = larRange * (-1)

        num = str(abs(x))

        reversenum = num[::-1]
        if x<0:
            final = int(reversenum)*(-1)
        else:
            final = int(reversenum)
            
        if final>larRange or final<smaRange:
            final = 0
            
        return final

solution = Solution()
print(solution.reverse(-123))
