from collections import Counter

def solution(participant, completion):
    # 참가자의 이름을 카운트
    count = Counter(participant)
    # 완주한 선수의 이름을 카운트에서 감소
    for name in completion:
        count[name] -= 1
    
    # 카운트가 0이 아닌, 즉 완주하지 못한 선수 찾기
    for name in count:
        if count[name] > 0:
            return name