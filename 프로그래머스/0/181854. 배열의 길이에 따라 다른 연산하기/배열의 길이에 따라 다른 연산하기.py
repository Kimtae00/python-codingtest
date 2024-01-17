def solution(arr, n):
    # arr 배열의 길이가 홀수인 경우
    if len(arr) % 2 != 0:
        return [x + n if i % 2 == 0 else x for i, x in enumerate(arr)]
    # arr 배열의 길이가 짝수인 경우
    else:
        return [x + n if i % 2 != 0 else x for i, x in enumerate(arr)]