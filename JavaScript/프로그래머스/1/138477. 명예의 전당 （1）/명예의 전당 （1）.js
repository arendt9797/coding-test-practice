function solution(k, score) {
    let fame = []
    return score.reduce((acc, cur) => {
        fame.push(cur)
        fame = fame.sort((a, b)=>b - a).splice(0, k)
        acc.push(Math.min(...fame))
        return acc
    }, [])
}