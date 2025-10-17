def solution(money):
    answer = []
    count = money//5500
    extra = money%5500
    
    answer.append(count)
    answer.append(extra)
    return answer