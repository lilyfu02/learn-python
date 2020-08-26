from typing import List


class Solution():
    def assign(self, g: List[int], j: List[int]) -> int:
        child, turn = 0, 0
        g.sort()
        j.sort()
        while child < len(g) and turn < len(j):
            if g[child] <= j[turn]:
                child += 1
            turn += 1
        return child


solution = Solution()
p = [1, 2]
c = [1, 2, 3]
print(solution.assign(p, c))
