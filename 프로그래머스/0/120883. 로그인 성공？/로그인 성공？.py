def solution(id_pw, db):
    answer = ''
    flag=0
    for i in db:
        if id_pw[0] == i[0] and id_pw[1]==i[1]:
            answer = 'login'
        elif id_pw[0] == i[0] and id_pw[1]!=i[1]:
            answer = 'wrong pw'
            flag=1
        else:
            answer = 'fail'
    if flag==1:
        answer = 'wrong pw'
    return answer