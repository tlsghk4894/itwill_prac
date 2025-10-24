def solution(dots):
    answer = 0
    h=0
    w=0
    first = dots[0]
    for i in dots:
        print(i,first)
        if i[0] != first[0] and w==0:
            if i[0]>first[0]:
                w=i[0]-first[0]
            else:
                w=first[0]-i[0]
        if i[1] != first[1] and h==0:
            if i[1] > first[1]:
                h=i[1]-first[1]
            else:
                h=first[1]-i[1]
            
    answer = h*w
    return answer