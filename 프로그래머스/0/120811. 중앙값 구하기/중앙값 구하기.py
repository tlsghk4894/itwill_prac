import math
def solution(array):
    answer = 0
    sorted_array=sorted(array)
    mid = int(len(sorted_array)/2)
    print(sorted_array,mid)
    answer=sorted_array[mid]
    return answer