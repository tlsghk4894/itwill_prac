def solution(spell, dic):
    answer = 0
    for i in dic:
        count=0
        for j in spell:
            if j in i:
                count+=1
                print(count,len(spell))
                if count==len(spell):
                    break

        if count==len(spell):
            answer=1
            break
        else:
            answer=2
    return answer