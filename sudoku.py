#! /usr/bin/python
import random
from Numberjack import *

class Sudoku(object):
	"""
	Class: Sudoku
	
	Sudoku represents a 9 by 9 sudoku grid.
	"""
	def __init__(self):
		"""
		Invocation: Sudoku()
		Meaning: Construct a list of lists full of zeros and a 9 by 9 matrix with a few givens in place.
		Preconditions: None.
		Postconditions: The returned value is a matrix in the form a sudoku grid with blanks as zeros.
		
		>>> import random
		>>> numbers = [0, 1, 6, 0, 2, 9, 0, 5, 2, 0, 8, 1, 1, 4, 3, 1, 7, 6, 2, 1, 7, 3, 8, 8, 4, 1, 1, 4, 7, 4, 5, 1, 9, 5, 2, 2, 5, 5, 5, 7, 0, 4, 7, 1, 2, 7, 6, 3, 8, 3, 3, 0, 1, 6, 0, 2, 9, 0, 5, 2]
		>>> random.randint = lambda min, max: numbers.pop(0)
		>>> import __builtin__ 
		>>> answers = ['']
		>>> __builtin__.raw_input = lambda message: answers.pop(0)
		>>> Sudoku()
		[[0, 6, 9, 0, 0, 2, 0, 0, 1],
		 [0, 0, 0, 0, 3, 0, 0, 6, 0],
		 [0, 7, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 8],
		 [0, 1, 0, 0, 0, 0, 0, 4, 0],
		 [0, 9, 2, 0, 0, 5, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [4, 2, 0, 0, 0, 0, 3, 0, 0],
		 [0, 0, 0, 3, 0, 0, 0, 0, 0]]
		[[3, 6, 9, 5, 4, 2, 8, 7, 1],
		 [1, 4, 5, 8, 3, 7, 2, 6, 9],
		 [2, 7, 8, 9, 6, 1, 4, 5, 3],
		 [5, 3, 4, 1, 9, 6, 7, 2, 8],
		 [8, 1, 6, 7, 2, 3, 9, 4, 5],
		 [7, 9, 2, 4, 8, 5, 1, 3, 6],
		 [6, 8, 3, 2, 7, 9, 5, 1, 4],
		 [4, 2, 1, 6, 5, 8, 3, 9, 7],
		 [9, 5, 7, 3, 1, 4, 6, 8, 2]]
		All Done
		"""
		self._matrix = Matrix(9, 9, 1, 9)
		"""
		Field: _matrix
		Type: _matrix is a 9 by 9 Matrix
		Meaning: _matrix is a Matrix that more easily works with Numberjack to create and solve the puzzle.
		Invariants: _matrix is a 9 by 9 Matrix that only uses numbers 1 through 9.
		"""
		self._contents = [[0 for i in range(9)] for j in range(9)]
		"""
		Field: _contents
		Type: _contents is a list of lists.
		Meaning: _contents is a List of Lists that creates a grid.
		Invariants: _contents is a List of 9 Lists of length 9.
		"""
		self._model = Model()
		"""
		Field: _model
		Type: _model is a Model.
		Meaning: _model helps place numbers into _matrix.
		Invariants: None.
		"""
		for s in range(20): # places givens into the puzzle
			column = random.randint(0, 8)
			row = random.randint(0, 8)
			value = random.randint(1, 9)
			self._contents[column][row] = value
		for i in range(9): # The following are the rules of the game for the program to follow
			self._model.add(AllDiff([self._matrix[i, j] for j in range(9)]))
			self._model.add(AllDiff([self._matrix[j, i] for j in range(9)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(3) for j in range(3)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(3, 6) for j in range(3)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(6, 9) for j in range(3)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(3) for j in range(3, 6)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(3, 6) for j in range(3, 6)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(6, 9) for j in range(3, 6)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(3) for j in range(6, 9)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(3, 6) for j in range(6, 9)]))
		self._model.add(AllDiff([self._matrix[i, j] for i in range(6, 9) for j in range(6, 9)]))
		for row in range(9): # Places numbers where the givens are not
			for column in range(9):
				if self._contents[row][column] != 0:
					self._model.add(self._matrix[row, column] == self._contents[row][column])
		self._solve()
	def _solve(self):
		"""
		Invocation: _solve()
		Meaning: _solve solves the puzzle and prints the solution when the user decides to.
		Preconditions: There is a puzzle to solve
		Postconditions: The result is the solved puzzle.
		"""
		solver = self._model.load('Mistral')
		if solver.solveAndRestart():
			print Matrix(self._contents) # Prints the unsolved puzzle with givens
			raw_input('Solve the Puzzle?') # Prompts the user to see if they want the solution
			print self._matrix # Prints the solution
		else:
			self.__init__() # Reruns the function if a solution cannot be found
	def __repr__(self):
		"""
		Invocation: print Sudoku
		Meaning: prints the following string for testing purposes.
		Preconditions: None.
		Postconditions: The returned value is the following string.
		"""
		return 'All Done'

Sudoku()		
"""
Class: Grid

Fields:

Field: _contents
Type: _contents is a list of lists.
Meaning: _contents is a List of Lists that creates a grid.
Invariants: _contents is a List of 9 Lists of length 9.

Field: _matrix
Type: _matrix is a 9 by 9 Matrix
Meaning: _matrix is a Matrix that more easily works with Numberjack to create and solve the puzzle.
Invariants: _matrix is a 9 by 9 Matrix that only uses numbers 1 through 9.

Field: _model
Type: _model is a Model.
Meaning: _model helps place numbers into _matrix.
Invariants: None.

Methods:

Invocation: Sudoku()
Meaning: Construct a list of lists full of zeros and a 9 by 9 matrix with a few givens in place.
Preconditions: None.
Postconditions: The returned value is a matrix in the form a sudoku grid with blanks as zeros.

Invocation: _solve()
Meaning: _solve solves the puzzle when the user decides to.
Preconditions: There is a puzzle to solve
Postconditions: The result is the solved puzzle.

Invocation: print Sudoku
Meaning: prints the following string for testing purposes.
Preconditions: None.
Postconditions: The returned value is the following string.
"""
