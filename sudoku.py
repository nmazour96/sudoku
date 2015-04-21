#! /usr/bin/python
from __future__ import division
import math
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
	
	def _put(row, column, value):
		"""
		Invocation: ._put(row, column, value)
		Meaning: Put a value into a specified place in the grid.
		Preconditions: row and column are each a number 0 through 8 and value is a number 1 through 9 and there is not already a value at that location.
		Postconditions: The result is None and value is placed at the coordinates.
		"""
		if self.contents[row[column]] == None:
			self._contents[row[column]] = value
		return repr(['There is already a value at ' + self._contents[row[column]]])

	

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
Postconditions: The result is None and value is either placed or discarded.

Invocation: print Grid
Meaning: print _contents so that it forms a 9 by 9 grid.
Preconditions: None
Postconditions: The returned value is the List of Lists formed into a grid.
"""