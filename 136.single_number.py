def singleNumber(nums):
    singles = []
    for i in nums:
        if i in singles:
            singles.remove(i)
        else:
            singles.append(i)
    return singles[0]


print(singleNumber([2,2,1]))