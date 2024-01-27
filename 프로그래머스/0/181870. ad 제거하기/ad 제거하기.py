def solution(strArr):
    # "ad" 부분 문자열을 포함하지 않는 문자열만 필터링하여 새 리스트를 생성
    filtered = [s for s in strArr if "ad" not in s]
    return filtered