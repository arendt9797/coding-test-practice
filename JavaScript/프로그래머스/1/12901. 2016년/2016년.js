function solution(a, b) {
    const dates = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31, 
        6: 30,
        7: 31, 
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    const days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    let totalDays = 0
    for (month in dates) {
        if (month === String(a)) {
            totalDays += b
            totalDays -= 1
            break
        }
        totalDays += dates[month]
    }
    console.log(totalDays)
    return days[totalDays%7]
}