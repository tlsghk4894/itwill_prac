def solution(before, after):
    answer = 0
    count_before_dic={}
    count_after_dic={}
    for i in before:
        if i in count_before_dic:
            count_before_dic[i]+=1
        else:
            count_before_dic[i]=1
    print(count_before_dic)
    for i in after:
        if i in count_after_dic:
            count_after_dic[i]+=1
        else:
            count_after_dic[i]=1
    print(count_after_dic)
    
    if count_after_dic==count_before_dic:
        answer=1
    else:
        answer=0
    return answer