#! /usr/bin/python
import random
from Numberjack import *
import numpy as np

class Grid(object):
	"""
	Class: Grid
	
	Grid represents a 9 by 9 sudoku grid.
	"""
	def __init__(self, list):
		"""
		Invocation: Grid(list)
		Meaning: Construct a grid with a list of lists.
		Preconditions: list should be a List of 9 Lists of length 9.
		Postconditions: The returned value is a 9 by 9 grid.
		"""
		self._contents = # [[0 for i in range(9)] for j in range(9)] change to matrix  numberjack.Matrix(9, 9)?
		for i in range(9):
			for j in range(9):
				self._contents[i][j] = random.randint(1, 9)
				self._check()
		"""
		Field: _contents
		Type: _contents is a list of lists.
		Meaning: _contents is a List of Lists that creates a grid.
		Invariants: _contents is a List of 9 Lists of length 9.
		"""
	def _check(self):
		model = Model(
			AllDiff([self._contents[0][c] for c in range(9)]),
			AllDiff([self._contents[1][c] for c in range(9)]),
			AllDiff([self._contents[2][c] for c in range(9)]),
			AllDiff([self._contents[3][c] for c in range(9)]),
			AllDiff([self._contents[4][c] for c in range(9)]),
			AllDiff([self._contents[5][c] for c in range(9)]),
			AllDiff([self._contents[6][c] for c in range(9)]),
			AllDiff([self._contents[7][c] for c in range(9)]),
			AllDiff([self._contents[8][c] for c in range(9)]),
			AllDiff([self._contents[c][0] for c in range(9)]),
			AllDiff([self._contents[c][1] for c in range(9)]),
			AllDiff([self._contents[c][2] for c in range(9)]),
			AllDiff([self._contents[c][3] for c in range(9)]),
			AllDiff([self._contents[c][4] for c in range(9)]),
			AllDiff([self._contents[c][5] for c in range(9)]),
			AllDiff([self._contents[c][6] for c in range(9)]),
			AllDiff([self._contents[c][7] for c in range(9)]),
			AllDiff([self._contents[c][8] for c in range(9)]),
			AllDiff([self._contents[c][d] for c in range(3) for d in range(3)]),
			AllDiff([self._contents[c][d] for c in range(3, 6) for d in range(3)]),
			AllDiff([self._contents[c][d] for c in range(6, 9) for d in range(3)]),
			AllDiff([self._contents[c][d] for c in range(3) for d in range(3, 6)]),
			AllDiff([self._contents[c][d] for c in range(3, 6) for d in range(3, 6)]),
			AllDiff([self._contents[c][d] for c in range(6, 9) for d in range(3, 6)]),
			AllDiff([self._contents[c][d] for c in range(3) for d in range(6, 9)]),
			AllDiff([self._contents[c][d] for c in range(3, 6) for d in range(6, 9)]),
			AllDiff([self._contents[c][d] for c in range(6, 9) for d in range(6, 9)])
			)
		return model, self._contents
	
	def _solve(self, param):
		

	def __repr__(self):
		"""
		Invocation: print Grid
		Meaning: print _contents so that it forms a 9 by 9 grid.
		Preconditions: None
		Postconditions: The returned value is the List of Lists formed into a grid.
		"""
		result = ""
		for i in range(9):
			result = result + str(self._contents[i]) + "\n"
		return result

random.randint(1, 9) # stores a random number between, and including, 1 and 9.

e = Grid([])
print e

"""
Class: Grid

Fields:

Field: _contents
Type: _contents is a list of lists.
Meaning: _contents is a List of Lists that creates a grid.
Invariants: _contents is a List of 9 Lists of length 9.

Methods:

Invocation: Grid(list)
Meaning: Construct a grid with a list of lists.
Preconditions: list should be a List of 9 Lists of length 9.
Postconditions: The returned value is a 9 by 9 grid.

Invocation: ._put(row, column, value)
Meaning: Put a value into a specified place in the grid.
Preconditions: row and column are each a number 0 through 8 and value is a number 1 through 9.
Postconditions: The result is None and value is placed at the coordinates.

Invocation: ._check_row(row, value)
Meaning: Check that there is not already value in that row.
Preconditions: row is a number 0 through 8 and value is a number 1 through 9.
Postconditions: The result is True if there is not the same number in that row and False otherwise.

Invocation: ._check_column(column, value)
Meaning: Check that there is not already value in that column.
Preconditions: column is a number 0 through 8 and value is a number 1 through 9.
Postconditions: The result is True if there is not the same number in that column and False otherwise.

Invocation: print Grid
Meaning: print _contents so that it forms a 9 by 9 grid.
Preconditions: None
Postconditions: The returned value is the List of Lists formed into a grid.
"""
