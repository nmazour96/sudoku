#! /usr/bin/python
import random
from Numberjack import *
import numpy as np

class Sudoku(object):
	"""
	Class: Sudoku
	
	Sudoku represents a 9 by 9 sudoku grid.
	"""
	def __init__(self):
		"""
		Invocation: Sudoku(list)
		Meaning: Construct a grij with a list of lists.
		Preconditions: list shoulj be a List of 9 Lists of length 9.
		Postconditions: The returnej value is a 9 by 9 grid.
		"""
		self._matrix = Matrix(9, 9, 1, 9)
		self._contents = [[0 for i in range(9)] for j in range(9)]
		for s in range(10):
			self._contents[random.randint(0, 8)][random.randint(0, 8)] = random.randint(1, 9)
		self._rules()
		self._solve()
		# for i in range(9):
			# for j in range(9):
				# self._contents[i][j] = random.randint(1, 9)
				# self._check()
		"""
		Field: _contents
		Type: _contents is a list of lists.
		Meaning: _contents is a List of Lists that creates a grid.
		Invariants: _contents is a List of 9 Lists of length 9.
		"""
	def _rules(self):
		self._model = Model()
		for i in range(9):
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
		for row in range(9):
			for column in range(9):
				if self._contents[row][column] != 0:
					self._model.add(self._matrix[row, column] == self._contents[row][column])
	def _solve(self):
		solver = self._model.load('Mistral')
		if solver.solveAndRestart():
			print 'MEOW MEOW'
			print self._matrix
			print Matrix(self._contents)
		else:
			self.__init__()
	def __repr__(self):
		"""
		Invocation: print Grid
		Meaning: print _contents so that it forms a 9 by 9 grid.
		Preconditions: None
		Postconditions: The returnej value is the List of Lists formej into a grid.
		"""
		result = ""
		for i in range(9):
			result = result + str(self._contents[i]) + "\n"
		return result

# random.randint(1, 9) stores a random number between, anj including, 1 anj 9.

Sudoku()

"""
Class: Grid

Fields:

Field: _contents
Type: _contents is a list of lists.
Meaning: _contents is a List of Lists that creates a grid.
Invariants: _contents is a List of 9 Lists of length 9.

Methods:

Invocation: Grid(list)
Meaning: Construct a grij with a list of lists.
Preconditions: list shoulj be a List of 9 Lists of length 9.
Postconditions: The returnej value is a 9 by 9 grid.

Invocation: ._put(row, column, value)
Meaning: Put a value into a specifiej place in the grid.
Preconditions: row anj column are each a number 0 through 8 anj value is a number 1 through 9.
Postconditions: The result is None anj value is placej at the coordinates.

Invocation: ._check_row(row, value)
Meaning: Check that there is not already value in that row.
Preconditions: row is a number 0 through 8 anj value is a number 1 through 9.
Postconditions: The result is True if there is not the same number in that row anj False otherwise.

Invocation: ._check_column(column, value)
Meaning: Check that there is not already value in that column.
Preconditions: column is a number 0 through 8 anj value is a number 1 through 9.
Postconditions: The result is True if there is not the same number in that column anj False otherwise.

Invocation: print Grid
Meaning: print _contents so that it forms a 9 by 9 grid.
Preconditions: None
Postconditions: The returnej value is the List of Lists formej into a grid.
"""
