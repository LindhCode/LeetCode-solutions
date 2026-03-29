# Medium problem

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        grouped = {}
        
        for i in range(len(groupSizes)):
            grouped.setdefault(groupSizes[i],[])
            grouped[groupSizes[i]].append(i)

        result = []
        for j in grouped:
            if len(grouped[j]) != j:
                a = [grouped[j][i:i + j] for i in range(0, len(grouped[j]), j)]
                for k in a:
                    result.append(k)
            else:
                result.append(grouped[j])
        return result
        
S = Solution
print(S.groupThePeople(S, [2,1,3,3,3,2,3,3,3]))
