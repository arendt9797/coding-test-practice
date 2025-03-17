def solution(s):
    nums = s.split(' ')
    nums = [int(n) for n in nums]
    nums.sort()
    return str(nums[0]) + ' ' + str(nums[-1])
    