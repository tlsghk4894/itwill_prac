def solution(order):
    answer = 0
    str_order=list(str(order))
    for i in range(0,len(str_order)):
        if str_order[i]=='3' or str_order[i]=='6' or str_order[i]=='9' :
            answer+=1
    return answer