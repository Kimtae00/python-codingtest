def solution(s):
    # 스택 초기화
    stack = [] 

    for bracket in s:
        # 여는 괄호 => 스택에 추가
        if bracket == '(':  
            stack.append(bracket)
        # 닫는 괄호
        else:
            # 스택이 비어있지 않고, 짝이 맞는 여는 괄호가 있으면
            if stack and stack[-1] == '(':  
                # 짝지어진 여는 괄호를 스택에서 제거
                stack.pop() 
            else:
                # 짝이 맞지 않는 경우 False 반환
                return False  
            
    # 모든 문자열을 순회한 후에 스택이 비어있으면 True, 아니면 False 반환
    return len(stack) == 0  