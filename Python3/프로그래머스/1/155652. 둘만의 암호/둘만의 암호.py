def solution(s, skip, index):
    valid = [chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in skip]*2
    answer = ''
    
    for c in s:
        cur_idx = valid.index(c)
        target_idx = cur_idx + index
        if target_idx >= len(valid):
            target_idx -= len(valid)
        answer += valid[target_idx]
    
    return answer