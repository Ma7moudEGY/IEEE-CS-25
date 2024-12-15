def Solution(board, row, col_flags, diag1_flags, diag2_flags, count):
    if row == 8:
        count[0] += 1
        return
    
    for col in range(8):
        if board[row][col] == '*' or col_flags[col] == True or diag1_flags[row - col + 7] == True or diag2_flags[row + col] == True:
            continue

        col_flags[col] = True
        diag1_flags[row - col + 7] = True
        diag2_flags[row + col] = True

        Solution(board, row + 1, col_flags, diag1_flags, diag2_flags, count)

        col_flags[col] = False
        diag1_flags[row - col + 7] = False
        diag2_flags[row + col] = False


Board = []

for _ in range(8):
    row = input().strip()
    Board.append(row)

ColFlags = [False for _ in range(8)]
Diag1Flags = [False for _ in range(15)]
Diag2Flags = [False for _ in range(15)]
Count = [0]


Solution(Board, 0, ColFlags, Diag1Flags, Diag2Flags, Count)

print(Count[0])