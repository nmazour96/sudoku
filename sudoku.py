#! /usr/bin/python
from __future__ import division
import math
import random
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
		self._contents = [[None for i in range(9)] for j in range(9)]
		"""
		Field: _contents
		Type: _contents is a list of lists.
		Meaning: _contents is a List of Lists that creates a grid.
		Invariants: _contents is a List of 9 Lists of length 9.
		"""
	def _fill(self):
		for i in range(9):
			for j in range(9):
				self._contents[i[j]] = random.randint(1,9)


	def _check_row(self, row, value):
		"""
		Invocation: ._check_row(row, value)
		Meaning: Check that there is not already value in that row.
		Preconditions: row is a number 0 through 8 and value is a number 1 through 9.
		Postconditions: The result is True if there is not the same number in that row and False otherwise.
		"""
		i = 0
		while i <= 9:		
			if value != self._contents[row[i]]:
				i = i + 1
			else:
				return False
		return True
	def _check_column(self, column, value):
		"""
		Invocation: ._check_column(column, value)
		Meaning: Check that there is not already value in that column.
		Preconditions: column is a number 0 through 8 and value is a number 1 through 9.
		Postconditions: The result is True if there is not the same number in that column and False otherwise.
		"""
		while i <= 9:
			if value != self._contents[i[column]]:
				i = i + 1
			else:
				return False
		return True
				
	def _put(self, row, column):
		"""
		Invocation: ._put(row, column, value)
		Meaning: Put a value into a specified place in the grid.
		Preconditions: row and column are each a number 0 through 8 and value is a number 1 through 9 and there is not already a value at that location.
		Postconditions: The result is None and value is placed at the coordinates.
		"""
		value = 7
		if self._check_row(row, value) == False:
			return repr(['There is already a ' + value + ' in this row'])
		if self._check_column(column, value) == False:
			return repr(['There is already a ' + value + ' in this column'])
		if self._contents[row[column]] == None:
			self._contents[row[column]] = value
		return repr(['There is already a value at ' + self._contents[row[column]]])
				
	def __repr__(self):
		"""
		Invocation: print Grid
		Meaning: print _contents so that it forms a 9 by 9 grid.
		Preconditions: None
		Postconditions: The returned value is the List of Lists formed into a grid.
		"""
		return repr(self._contents)

random.randint(1, 9) # stores a random number between, and including, 1 and 9.

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
