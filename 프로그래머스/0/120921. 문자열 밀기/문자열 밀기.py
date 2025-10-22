def solution(A, B):
    answer = 0
    new_A=''
    if A!=B:
        while new_A !=B:
            answer+=1
            new_A=''
            for i in range(0,len(A)):
                new_A += A[(i-1)%len(A)]
            A=new_A
            print(new_A)
            if answer > len(A):
                return -1
            if new_A == B:
                return answer
    else:
        return 0
    return answer