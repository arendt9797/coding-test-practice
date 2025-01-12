function solution(k, m, score) {
    score.sort().reverse()
    let answer = 0
    let idx = m-1
    while (idx < score.length) {
        answer += score[idx]
        idx += m
    }
    return answer*m
}