def solution(n):
    if(n<=7):
        answer = 1
    elif(n>7 and n%7!=0):
        answer = n//7+1
    else:
        answer = n//7
    return int(answer)