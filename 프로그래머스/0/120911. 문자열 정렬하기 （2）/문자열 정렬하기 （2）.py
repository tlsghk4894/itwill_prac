def solution(my_string):
    answer = ''
    lower_my_string=my_string.lower()
    print(lower_my_string)
    sorted_my_string=sorted(lower_my_string)
    print(sorted_my_string)
    for i in sorted_my_string:
        answer += i
    print(answer)
        
    return answer