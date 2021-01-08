# sudoku solver

"""def find_next_empty(puzzle):
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == 0:
				return r,c
	return None, None

def is_valid(puzzle, guess, row, col):
	
	row_vals = puzzle[row]
	if guess in row_vals:
		return False

	col_vals = [puzzle[i][col] for i in range(9)]
	if guess in col_vals:
		return False

	row_start = (row // 3) * 3 
	col_start = (col // 3) * 3

	for r in range(row_start, row_start + 3):
		for c in range(col_start, col_start + 3):
			if puzzle[r][c] == guess:
				return False

	return True



def solve_sudoku(puzzle):

	row, col = find_next_empty(puzzle)

	if row is None:
		return True

	for guess in range(1,10):
		if is_valid(puzzle, guess, row, col):
			puzzle[row][col] = guess

			if solve_sudoku(puzzle):
				return True

		puzzle[row][col] = 0

	return False



puzzle = [

		[6,0,0, 0,0,0, 0,1,7],
		[0,0,0, 0,2,9, 3,5,0],
		[0,0,4, 0,0,6, 8,0,0],
		[8,0,0, 0,0,0, 9,0,0],
		[0,0,0, 5,0,1, 0,0,0],
		[0,0,2, 0,0,0, 0,0,4],
		[0,0,5, 1,0,0, 2,0,0],
		[0,8,7, 9,3,0, 0,0,0],
		[4,6,0, 0,0,0, 0,0,9],
]


x = [

		[6,0,0, 0,0,0, 0,1,7],
		[0,0,0, 0,2,9, 3,5,0],
		[0,0,4, 0,0,6, 8,0,0],
		[8,0,0, 0,0,0, 9,0,0],
		[0,0,0, 5,0,1, 0,0,0],
		[0,0,2, 0,0,0, 0,0,4],
		[0,0,5, 1,0,0, 2,0,0],
		[0,8,7, 9,3,0, 0,0,0],
		[4,6,0, 0,0,0, 0,0,9],
]

print(solve_sudoku(x))
print(x)"""



def find_next(board):
	for r in range(9):
		for c in range(9):
			if board[r][c] == 0:
				return r, c
	return None, None

def is_valid(num, board, row, col):
	# in row
	if num in board[row]:
		return False

	# in column
	for i in board:
		if num == i[col]:
			return False

	# in 3x3 square
	col_start = (col // 3) * 3 
	row_start = (row // 3) * 3

	for r in range(row_start, row_start+3):
		for c in range(col_start, col_start+3):
			if board[r][c] == num:
				return False

	return True




def solve_sudoku(board):
	row, col = find_next(board)

	if row == None:
		return True

	for num in range(1,10):
		if is_valid(num, board, row, col):

			board[row][col] = num

			if solve_sudoku(board):
				return True

	board[row][col] = 0

	return False


x = [

		[6,0,0, 0,0,0, 0,1,7],
		[0,0,0, 0,2,9, 3,5,0],
		[0,0,4, 0,0,6, 8,0,0],
		[8,0,0, 0,0,0, 9,0,0],
		[0,0,0, 5,0,1, 0,0,0],
		[0,0,2, 0,0,0, 0,0,4],
		[0,0,5, 1,0,0, 2,0,0],
		[0,8,7, 9,3,0, 0,0,0],
		[4,6,0, 0,0,0, 0,0,9],
]

print(solve_sudoku(x))

for r in range(9):
	l = []
	for c in range(9):
		l.append(x[r][c])
		if c in [2,5]:
			l.append("|")
	if r in [3,6]:
		print("- "*11)
	print("".join(str(i)+" " for i in l))

				




















