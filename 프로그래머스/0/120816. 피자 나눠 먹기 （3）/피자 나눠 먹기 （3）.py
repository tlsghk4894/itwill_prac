def solution(slice, n):
    answer=0
    if(slice<n and n%slice!=0):
        answer = n//slice+1
    elif(slice>=n):
        answer=1
    else:
        answer = n//slice
    return int(answer)