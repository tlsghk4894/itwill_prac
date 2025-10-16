# def solution(chicken):
#     coupon=0
#     answer=0
#     while(chicken>0):
#         answer+=chicken//10
#         coupon += chicken%10
#         print('answer,coupon',answer,coupon)
#         if(coupon>=10):
#             print('coupon이 10장 모였음',coupon)
#             answer+=1
#             print('answer',answer)
#             coupon=0
#         chicken = chicken//10
#     return answer

def solution(chicken):
    answer = 0 
    coupon = chicken
    
    while coupon >= 10:
        service_chicken = coupon // 10
        answer += service_chicken
        remaining_coupon = coupon % 10
        coupon = remaining_coupon + service_chicken
        
    return answer