def solution(array, n):
    answer = 0
    count=0
    for i in array:
        if(i==n):
            count+=1
    return count