def solution(my_string, letter):
    answer = ''
    my_string = list(my_string)
    for i in range(0,len(my_string)):
        print(my_string[i],letter)
        if my_string[i] != letter:
            answer+=my_string[i]
        
    return answer