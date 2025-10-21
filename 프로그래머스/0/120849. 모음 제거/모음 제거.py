def solution(my_string):
    answer = ''
    answer = my_string
    for i in my_string:
        if i in ('a','e','i','o','u'):
            print(i)
            answer=answer.replace(i,'')
            print(answer)
    return answer