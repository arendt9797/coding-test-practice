function solution(s) {
    const sObj = {}
    const answer = []
    s.split('').forEach((char, i) => {
        sObj.hasOwnProperty(char) ? answer.push(i - sObj[char]) : answer.push(-1)
        sObj[char] = i
    })
    
    return answer
}