import tkinter as tk


def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3)
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        grid[i][j] = 0
        return False


#input = [
#    [8, 0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 3, 6, 0, 0, 0, 0, 0],
#    [0, 7, 0, 0, 9, 0, 2, 0, 0],
#    [0, 5, 0, 0, 0, 7, 0, 0, 0],
#    [0, 0, 0, 0, 4, 5, 7, 0, 0],
#    [0, 0, 0, 1, 0, 0, 0, 3, 0],
#    [0, 0, 1, 0, 0, 0, 0, 6, 8],
#    [0, 0, 8, 5, 0, 0, 0, 1, 0],
#    [0, 9, 0, 0, 0, 0, 4, 0, 0]]



class SudokuGrid(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Sudoku Grid")
		self.geometry("300x300")

		self.entries = [[tk.Entry(self, width=2) for _ in range(9)] for _ in range(9)]
		for i, row in enumerate(self.entries):
			for j, entry in enumerate(row):
				entry.grid(row=i, column=j)

		self.save_button = tk.Button(self, text="Save", command=self.save_grid)
		self.save_button.grid(row=10, columnspan=9)

	def save_grid(self):
		input = [[int(entry.get()) if entry.get().isdigit() else 0 for entry in row] for row in self.entries]
		solveSudoku(input)
		print(input)



if __name__ == "__main__":
	app = SudokuGrid()
	app.mainloop()
