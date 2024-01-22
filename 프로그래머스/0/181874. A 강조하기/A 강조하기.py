def solution(myString):
    return ''.join(x.upper() if x == 'a' else x.lower() if x.isupper() and x != 'A' else x for x in myString)