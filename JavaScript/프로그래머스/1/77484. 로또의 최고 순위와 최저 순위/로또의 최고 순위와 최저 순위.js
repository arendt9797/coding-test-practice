function solution(lottos, win_nums) {
    let unknown = 0
    let checked = 0
    let prize = [6, 6, 5, 4, 3, 2, 1]
    lottos.forEach(num => {
        if (!num) {
            unknown++
        } else if (win_nums.includes(num)) {
            checked++
        }
    })
    return [prize[checked+unknown], prize[checked]]
}