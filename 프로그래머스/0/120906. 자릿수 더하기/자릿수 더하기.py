def solution(n):
    answer = 0
    str_n = str(n)
    for i in range(0,len(str_n)):
        answer+=int(str_n[i])
    return answer