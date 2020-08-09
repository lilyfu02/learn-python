class Solution():
    def roman_number(self,s:str) -> int:
        general = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        final = 0

        for i in range(0,len(s)):
            final += general[s[i]]
            if i!=(len(s)-1):
                if s[i] == 'I':
                    if s [i+1] == 'V' or s[i+1] == 'X':
                        final -= 2
                if s[i] == 'X':
                    if s [i+1] == 'L' or s[i+1] == 'C':
                        final -= 20
                if s[i] == 'C':
                    if s [i+1] == 'D' or s[i+1] == 'M':
                        final -= 200

        return final

solution = Solution()
iinput = input("The roman number is: ")
print(solution.roman_number(iinput))
