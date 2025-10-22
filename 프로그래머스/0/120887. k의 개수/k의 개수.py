def solution(i, j, k):
    answer = 0
    a=[]
    for n in range(i,j+1):
        if str(k) in str(n):
            a.append(str(n).split())
        
    # print(a)
    for n in a:
        for m in n:
            for b in range(0,len(m)):
                if str(k) == m[b]:
                    answer+=1
    return answer