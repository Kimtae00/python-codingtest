def solution(arr, k):
    # 홀수인 경우
    if k % 2 != 0:
        answer = [x * k for x in arr]
    # 짝수인 경우
    else:
        answer = [x + k for x in arr]
    return answer
