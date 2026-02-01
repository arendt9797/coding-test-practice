from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    
    for part in participant:
        if p[part] != c[part]:
            return part