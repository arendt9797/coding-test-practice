def solution(s):
    answer = ''
    upper_flag = 1
    
    for char in s:
        if char == ' ':
            answer += char
            upper_flag = 1
            continue
        if upper_flag:
            answer += char.upper()
            upper_flag = 0
        else:
            answer += char.lower()
    
    return answer
        