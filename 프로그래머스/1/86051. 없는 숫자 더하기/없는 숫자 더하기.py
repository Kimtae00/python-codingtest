def solution(numbers):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum = 0
    for x in list:
        if x not in numbers:
            sum += x
    return sum