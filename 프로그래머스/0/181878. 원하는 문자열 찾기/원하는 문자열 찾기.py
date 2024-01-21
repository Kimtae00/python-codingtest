def solution(myString, pat):
    myString = myString.upper()
    pat = pat.upper()
    print(myString, pat)
    if pat in myString:
        return 1
    else:
        return 0