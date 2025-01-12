def solution(answers):
    n = len(answers)
    one = [1, 2, 3, 4, 5]*(n//5 + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5]*(n//8 + 1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(n//10 + 1)
    cnt = [0, 0, 0]
    
    for i in range(n):
        if one[i] == answers[i]:
            cnt[0] += 1
        if two[i] == answers[i]:
            cnt[1] += 1
        if three[i] == answers[i]:
            cnt[2] += 1
    ans = list(enumerate(cnt))
    ans.sort(key=lambda x: (-x[1], x[0]))
    highest_score = ans[0][1]
    ans = [x[0]+1 for x in ans if x[1] == highest_score]
    
    return ans