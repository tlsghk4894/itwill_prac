def solution(hp):
    answer=(hp//5)+((hp%5)//3)+1*((hp%5)%3)
    return int(answer)