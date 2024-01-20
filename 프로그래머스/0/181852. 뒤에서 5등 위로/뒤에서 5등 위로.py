def solution(num_list):
    # num_list를 오름차순으로 정렬
    sorted_list = sorted(num_list)
    # 가장 작은 5개의 수를 제외하고 반환
    return sorted_list[5:]
