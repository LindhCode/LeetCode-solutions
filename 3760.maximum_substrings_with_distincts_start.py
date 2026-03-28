class Solution:
    def maxDistinct(self, s: str) -> int:
        return len({x for x in set(s)})

S = Solution
print(S.maxDistinct(S,"aaaa"))