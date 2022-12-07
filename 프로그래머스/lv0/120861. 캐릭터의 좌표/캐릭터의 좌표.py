def solution(keyinput, board):
    column = board[0]
    row = board[1]
    answer = [0, 0]
    for i in keyinput:
        if i == "up" and answer[1]+1 <= (row // 2):
            answer[1] += 1
        if i == "down" and answer[1]-1 >= -(row // 2):
            answer[1] -= 1
        if i == "left" and answer[0]-1 >= -(column // 2):
            answer[0] -= 1
        if i == "right" and answer[0]+1 <= (column // 2):
            answer[0] += 1
    return answer