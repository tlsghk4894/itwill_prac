def solution(my_string):
    # my_string="aAb1B2cC34oOp"
    answer = 0
    count = 0
    flag=''
    for i in my_string:
        # print(i)
        if i.isnumeric():
            count+=1
            flag+=i
            print('flag : ',flag)
        elif flag:
            answer+=int(flag)
            print('answer : ', answer)
            flag=''
    if flag:
        answer+=int(flag)
    if count==0:
        return 0
    return answer