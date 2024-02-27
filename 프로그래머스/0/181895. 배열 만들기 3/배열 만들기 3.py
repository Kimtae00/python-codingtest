def solution(arr, intervals):
    
    first_interval = arr[intervals[0][0]:intervals[0][1] + 1]
    second_interval = arr[intervals[1][0]:intervals[1][1] + 1]

    
    new_array = first_interval + second_interval

    return new_array