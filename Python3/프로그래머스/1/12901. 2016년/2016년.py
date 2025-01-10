def solution(a, b):
    dates = {
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
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    total_days = 0
    for month in dates:
        if month == a:
            total_days += (b - 1)
            break
        total_days += dates[month]
    return days[total_days%7]
            