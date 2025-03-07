from collections import Counter  

def solution(survey, choices):
    counter = Counter()
    choices = [c-4 for c in choices]
    
    def addPoints(pair, point):
        first, second = [p for p in pair]
        if point > 0:
            counter[second] += point
        else:
            counter[first] -= point 
        return
    
    def compareType(left, right):
        if counter[left] >= counter[right]:
            return left
        else:
            return right
    
    for idx, pair in enumerate(survey):
        addPoints(pair, choices[idx])
    
    return ''.join([compareType('R', 'T'), compareType('C', 'F'), compareType('J', 'M'), compareType('A', 'N')])