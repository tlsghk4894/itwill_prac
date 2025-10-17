def solution(numbers, direction):
    answer = []
    answer=numbers.copy()
    for i in range(0,len(answer)):
        if direction == "right":
            print(numbers,answer,i,len(numbers),i%len(numbers))
            numbers[(i+1)%len(numbers)] = answer[i%len(numbers)]
        else:
            print(numbers,answer,i,len(numbers),i%len(numbers))
            numbers[(i-1)%len(numbers)] = answer[i%len(numbers)]
    answer=numbers
    return answer