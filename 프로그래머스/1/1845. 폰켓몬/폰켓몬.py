def solution(nums):
    num_types = len(set(nums))  # 폰켓몬 종류의 수
    num_select = len(nums) // 2  # 선택할 수 있는 폰켓몬의 수
    return min(num_types, num_select)  # 두 수 중 작은 값이 최대 폰켓몬 종류의 수
