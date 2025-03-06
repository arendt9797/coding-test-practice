def solution(ingredient):
    count = 0
    stack = []
    BURGER = [1, 2, 3, 1]
    
    for ing in ingredient:
        stack.append(ing)
        if len(stack) >= 4 and stack[-4:] == BURGER:
            count += 1
            del stack[-4:]
        
    return count