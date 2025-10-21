def solution(numbers):
    answer = ''
    stack =''
    for i in range(0,len(numbers)):
        if numbers[i:i+3] == 'one':
            answer+='1'
            print(numbers)
        elif numbers[i:i+3] == 'two':
            answer+='2'
        elif numbers[i:i+5] == 'three':
            answer+='3'
        elif numbers[i:i+4] == 'four':
            answer+='4'
        elif numbers[i:i+4] == 'five':
            answer+='5'
        elif numbers[i:i+3] == 'six':
            answer+='6'
        elif numbers[i:i+5] == 'seven':
            answer+='7'
        elif numbers[i:i+5] == 'eight':
            answer+='8'
        elif numbers[i:i+4] == 'nine':
            answer+='9'
        elif numbers[i:i+4] == 'zero':
            answer+='0'
    return int(answer)