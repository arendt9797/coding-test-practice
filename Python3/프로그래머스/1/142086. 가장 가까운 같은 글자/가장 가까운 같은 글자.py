from collections import defaultdict

def solution(s):
    sDict = defaultdict(str)
    answer = []
    
    for i, char in enumerate(s) :
        if char in sDict:
            answer.append(i - sDict[char])
        else:
            answer.append(-1)
        sDict[char] = i
        
    return answer