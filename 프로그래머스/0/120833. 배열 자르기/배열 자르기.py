def solution(numbers, num1, num2):
    answer = []
    for i in numbers:
        answer = numbers[num1:num2+1]
    return answer