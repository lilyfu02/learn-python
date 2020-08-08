class Solution:
    @staticmethod
    def base_seven(num: int) -> str:
        remainders = []
        x = abs(num)
        if x == 0:
            remainders = '0'
        else:
            while x > 0:
                remainders.append(str(x % 7))
                x //= 7
            remainders = ''.join(remainders[::-1])
            if num < 0:
                remainders = '-' + remainders
        return remainders


if __name__ == "__main__":
    n = input("num: ")
    print(Solution.base_seven(int(n)))
