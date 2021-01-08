# sudoku solver

# find the next empty box
def find_next(board):
	for r in range(9): # r = row
		for c in range(9): # c = column
			if board[r][c] == 0: 
				return r, c
	return None, None # if all boxes are full so return None and we know the puzzle solved

# Checking the number. Is number valid for the box
def is_valid(num, board, row, col):
	# in row
	if num in board[row]:
		return False

	# in column
	for i in board:
		if num == i[col]:
			return False
	# also we can use list comprehension here for checking column like this
	"""col_list = [i[col] for i in board]
	if num in col_list:
		return False"""

	# in 3x3 square
	col_start = (col // 3) * 3 # if you in 5 indexes  = 5 // 3 = 1,  1 * 3 = 3 so you can start checking from index 3 to index 5. its the second 3x3 square columns
	row_start = (row // 3) * 3

	for r in range(row_start, row_start+3):
		for c in range(col_start, col_start+3):
			if board[r][c] == num:
				return False

	return True  # if there is no False return True thats mean is the number is valid for  this box




def solve_sudoku(board):
	# find next empty location
	row, col = find_next(board)
	
	# if row is None you finished the puzzel so return True
	if row == None:
		return True
	
	# guess number and if its valid for box add to the box and go to the next box continue this until the number never valid for box
	# if you cant put the number box its return False and you come back the last box and add next valid number then you pass the next box
	# if all box full you finished the puzzle
	for num in range(1,10):
		if is_valid(num, board, row, col):

			board[row][col] = num

			if solve_sudoku(board):
				return True

	board[row][col] = 0

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

print(solve_sudoku(puzzle))

# print the solved sudoku
for r in range(9):
	l = []
	for c in range(9):
		l.append(puzzle[r][c])
		if c in [2,5]:
			l.append("|")
	if r in [3,6]:
		print("- "*11)
	print("".join(str(i)+" " for i in l))
