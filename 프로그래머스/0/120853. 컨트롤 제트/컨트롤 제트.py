def solution(s):
    answer = 0
    split_s = s.split()
    before_num = 0
    for i in split_s:
        if i.isnumeric():
            print(int(i))
            if int(i)>0:
                print(i)
                answer+=int(i)
                before_num=int(i)
        else:
            # print(i)
            if '-' in i:
                answer +=int(i)
                before_num = int(i)
            elif i=='Z':
                answer -=before_num
                
    return answer