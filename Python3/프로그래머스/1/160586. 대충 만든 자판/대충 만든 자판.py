from collections import defaultdict

def solution(keymap, targets):
    answer = []
    index_dict = defaultdict(int)
    for key in keymap:
        for i, k in enumerate(key):
            if k in index_dict:
                if index_dict[k] > i+1:
                    index_dict[k] = i+1
            else:
                index_dict[k] = i+1
    for target in targets:
        acc = 0
        for t in target:
            if t in index_dict:
                acc += index_dict[t]
            else:
                acc = -1
                break
        answer.append(acc)
    return answer