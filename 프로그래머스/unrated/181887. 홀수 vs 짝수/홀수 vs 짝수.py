def solution(num_list):
    oddSum = [num_list[x] for x in range(0, len(num_list)) if x % 2 != 0]
    evenSum = [num_list[x] for x in range(0, len(num_list)) if x % 2 == 0]

    oddSum = sum(oddSum)
    evenSum = sum(evenSum)
    return oddSum if oddSum >= evenSum else evenSum