def solution(num, k):
    answer = 1
    str_num = str(num)
    for i,v in enumerate(str_num):
        if v==str(k):
            return i+1
        else:
            answer=-1
    return answer