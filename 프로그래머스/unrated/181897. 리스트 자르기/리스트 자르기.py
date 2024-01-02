def solution(n, slicer, num_list):
    if n == 1:
        answer = [num_list[x] for x in range(0, slicer[1]+1)]
    elif n == 2:
        answer = [num_list[x] for x in range(slicer[0], len(num_list))]
    elif n == 3:
        answer = [num_list[x] for x in range(slicer[0], slicer[1]+1)]
    else:
        answer = [num_list[x] for x in range(slicer[0], slicer[1]+1, slicer[2])]
    return answer