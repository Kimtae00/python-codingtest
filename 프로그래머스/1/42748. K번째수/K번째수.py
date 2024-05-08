def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # array를 i부터 j까지 슬라이싱하여 자른 후 정렬
        sliced_array = sorted(array[i-1:j])
        # k번째 원소를 결과 리스트에 추가
        answer.append(sliced_array[k-1])
    return answer