function solution(s) {
    const len = s.length
    const midIdx = parseInt(len/2)
    return len % 2 ? s.substring(midIdx, midIdx+1) : s.substring(midIdx-1, midIdx+1)
}