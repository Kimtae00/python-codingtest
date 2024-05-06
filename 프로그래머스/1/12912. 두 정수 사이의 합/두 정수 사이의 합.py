def solution(a, b):
    sum = 0
    if a == b:
        return a
    elif a > b:
        for x in range(b, a+1):
            sum += x
        return sum
    else:
        for x in range(a, b+1):
            sum += x
        return sum
        