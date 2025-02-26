def solution(s):
    compare = [0, 0]
    cnt = 0
    first = s[0]
    
    for i, c in enumerate(s):
        if c == first:
            compare[0] += 1
        else:
            compare[1] += 1
        print(first, c, compare, cnt)
        if compare[0] == compare[1]:
            cnt += 1
            compare = [0, 0]
            if i != len(s)-1: 
                first = s[i+1]
    if compare[0] != compare[1]:
        cnt += 1
    return cnt