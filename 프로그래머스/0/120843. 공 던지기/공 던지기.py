def solution(numbers, k):
    answer= 0
    count= 0
    for i in range(0,len(numbers)*k+1):
        print('i%len(numbers):',i%len(numbers))
        if i%2==0:
            count+=1
            print(count,i)
            if count==k:
                answer=numbers[i%len(numbers)]
                return answer
    