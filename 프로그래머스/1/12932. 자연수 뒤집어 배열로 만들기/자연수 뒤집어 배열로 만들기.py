def solution(n):
    n = str(n)
    answer = [int(n[x]) for x in range(len(n)-1, -1, -1)]
    return answer