def solution(arr, idx):
    # idx 이후로 1인 가장 작은 인덱스를 찾기
    # idx 포함하여 검사
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1  # 1인 원소를 찾지 못한 경우 -1을 반환