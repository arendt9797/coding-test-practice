def solution(k, m, score):
    score.sort(reverse=True)
    answer, idx = 0, m-1
    while idx < len(score):
        answer += score[idx]
        idx += m
    return answer*m