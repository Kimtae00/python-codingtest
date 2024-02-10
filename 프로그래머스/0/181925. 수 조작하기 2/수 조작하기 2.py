def solution(numLog):
    answer = ''
    for x in range(0, len(numLog)-1):
        if numLog[x] - numLog[x+1] == -1:
            answer = answer + 'w'
        elif numLog[x] - numLog[x+1] == -10:
            answer = answer + 'd'
        elif numLog[x] - numLog[x+1] == 10:
            answer = answer + 'a'
        elif numLog[x] - numLog[x+1] == 1:
            answer = answer + 's'
            
    return answer