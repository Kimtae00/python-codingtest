def solution(n):
    count_one = bin(n).count('1')
    
    next_number = n + 1
    while True:
        count_one_next = bin(next_number).count('1')
        
        if count_one_next == count_one:
            return next_number
        
        next_number += 1