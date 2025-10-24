def solution(age):
    answer = ''
    str_age = str(age)
    
    for i in range(0,len(str_age)):
        if str_age[i]=='0':
            answer+='a'
        elif str_age[i]=='1':
            answer+='b'
        elif str_age[i]=='2':
            answer+='c'
        elif str_age[i]=='3':
            answer+='d'
        elif str_age[i]=='4':
            answer+='e'
        elif str_age[i]=='5':
            answer+='f'
        elif str_age[i]=='6':
            answer+='g'
        elif str_age[i]=='7':
            answer+='h'
        elif str_age[i]=='8':
            answer+='i'
        elif str_age[i]=='9':
            answer+='j'
            
    return answer