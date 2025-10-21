def solution(array):
    answer = 0
    str_array=str(array)
    for i in str_array:
        if i=='7':
            answer+=1
    return answer