def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency,reverse=True)
    print(sorted_emergency)
    result ={}
    for i,v in enumerate(sorted_emergency):
        result[i+1] = v
        
    for i in emergency:
        for key,value in result.items():
            if value == i:
                answer.append(key)
    print(result)
    return answer