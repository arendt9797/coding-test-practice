from itertools import combinations as cb

def solution(nums):
    result = 0
    
    def isPrime(number):
        n = number // 2
        for i in range(3, n + 1):
            if number % i == 0:
                return False
        return True

    nums = [sum(x) for x in list(cb(nums, 3))]
    for n in nums:
        if isPrime(n):
            result += 1
    
    return result