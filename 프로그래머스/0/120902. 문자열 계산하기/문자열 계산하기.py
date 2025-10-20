def solution(my_string):
    split_list = my_string.split(' ')    
    answer = int(split_list[0])
    
    for i in range(1, len(split_list), 2):
        operator = split_list[i]    
        number = int(split_list[i+1])
        
        if operator == '+':
            answer += number
        elif operator == '-':
            answer -= number 
            
    return answer