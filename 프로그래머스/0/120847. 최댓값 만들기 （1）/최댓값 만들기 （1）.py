def solution(numbers):
    answer = 0
    sorted_numbers = sorted(numbers)
    answer = sorted_numbers[-2]*sorted_numbers[-1]
    return answer