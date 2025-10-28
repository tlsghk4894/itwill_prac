def solution(array):
    answer = 0
    dict = {}

    for i in array:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
    print(dict)
    max_array = max(dict,key=dict.get)
    max_array_value = max(dict.values())
    print(max_array)
    print(max_array_value)
    count = 0
    for i,v in dict.items():
        if v == max_array_value:
            count+=1
    if count>1:
        answer=-1
    else:
        answer=max_array

    
    return answer