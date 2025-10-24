def solution(array):
    answer = []
    max = array[0]
    index=0
    for i in range(0,len(array)):
        if max<array[i]:
            max=array[i]
            index=i
    answer.append(max)
    answer.append(index)
    return answer