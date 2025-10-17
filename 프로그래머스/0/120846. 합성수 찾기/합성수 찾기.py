def solution(n):
    answer = 0
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count>=3):
            print(i)
            print('count값이 3 이상', count,answer)
            answer+=1
    return answer