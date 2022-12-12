def solution(quiz):
    answer = []
    for q in quiz:
        list = q.split()

        if list[1] == '+':
            if int(list[0]) + int(list[2]) == int(list[4]):
                answer.append('O')
            else:
                answer.append('X')
        elif list[1] == '-':
            if int(list[0]) - int(list[2]) == int(list[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer