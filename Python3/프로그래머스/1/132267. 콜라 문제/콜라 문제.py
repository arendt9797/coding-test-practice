def solution(a, b, n):
    answer = 0
    while n >= a:
        quota = n // a
        answer += quota * b
        n = quota * b + (n % a)
    return answer