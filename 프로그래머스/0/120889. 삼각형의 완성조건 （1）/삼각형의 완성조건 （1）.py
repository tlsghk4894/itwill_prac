def solution(sides):
    answer = 0
    sorted_sides=sorted(sides)
    if sorted_sides[-1]<(sorted_sides[0]+sorted_sides[1]):
        answer=1
    elif sorted_sides[-1]>=(sorted_sides[0]+sorted_sides[1]):
        answer=2
    return answer