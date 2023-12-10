nums, *boards = open(0).read().strip().split("\n\n")

nums = [int(x) for x in nums.split(",")]
boards = [[int(x) for x in board.split()] for board in boards]

lb = None
for num in nums:
    bi = 0
    while bi < len(boards):
        board = boards[bi]
        for i, n in enumerate(board):
            if n == num:
                board[i] = None
        if any(
            all(x == None for x in board[i * 5 : i * 5 + 5]) for i in range(5)
        ) or any(all(x == None for x in board[i::5]) for i in range(5)):
            lb = board
            del boards[bi]
        else:
            bi += 1
    if len(boards) == 0:
        break


print(sum(x or 0 for x in lb) * num)
