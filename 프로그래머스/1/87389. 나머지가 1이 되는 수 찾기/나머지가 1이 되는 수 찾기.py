def solution(n):
    answer = [num for num in range(2, n) if n % num == 1]
    return answer[0]