function solution(s1, s2) {
    let cnt = 0
    s1.forEach(char => {
        s2.includes(char) ? cnt++ : cnt
    })
    return cnt
}