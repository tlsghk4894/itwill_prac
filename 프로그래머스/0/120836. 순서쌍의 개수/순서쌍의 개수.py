# def solution(n):
#     answer = 0
#     for i in range(n+1):
#         for j in range(n+1):
#             if(i*j==n and i*j<=n):
#                 answer+=1
#     return answer

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=1
    return answer