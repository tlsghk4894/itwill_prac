def solution(my_string, num1, num2):
    answer = ''
    temp=''
    # for i in my_string:
    my_string=list(my_string)
    temp=my_string[num1]
    my_string[num1]=my_string[num2]
    my_string[num2]=temp
    answer=''.join(my_string)
    print(answer)
    return answer