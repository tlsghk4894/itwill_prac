# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     if denom2%denom1 ==0 and denom2>denom1:
#         numer1=numer1*(denom2//denom1)
#         denom1=denom1*(denom2//denom1)
#         answer.append(numer1+numer2)
#         answer.append(denom1)
#     elif denom1%denom2 ==0 and denom2<denom1:
#         numer2=numer2*(denom1//denom2)
#         denom2=denom2*(denom1//denom2)
#         answer.append(numer1+numer2)
#         answer.append(denom2)
#     else:
#         numer1= numer1*denom2
#         numer2=numer2*denom1
#         print(numer1,numer2)
#         denom1= denom1*denom2
        
#         answer.append(numer1+numer2)
#         answer.append(denom1)
#     return answer

# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     if denom2%denom1 ==0 and denom2>denom1:
#         numer1=numer1*(denom2//denom1)
#         denom1=denom1*(denom2//denom1)
#         answer.append(numer1+numer2)
#         answer.append(denom1)
#     elif denom1%denom2 ==0 and denom2<denom1:
#         numer2=numer2*(denom1//denom2)
#         denom2=denom2*(denom1//denom2)
#         answer.append(numer1+numer2)
#         answer.append(denom2)
#     else:
#         numer1= numer1*denom2
#         numer2=numer2*denom1
#         print(numer1,numer2)
#         denom1= denom1*denom2
        
#         answer.append(numer1+numer2)
#         answer.append(denom1)
#     return answer


def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1*denom2+numer2*denom1
    denom = denom1*denom2
    for i in range(2,numer+1):
        # print(numer,denom)
        if(numer%i==0 and denom%i==0):
            while numer % i == 0 and denom % i == 0:
                # print(i)
                numer //= i
                denom //= i
    answer.append(numer)
    answer.append(denom)
    return answer

