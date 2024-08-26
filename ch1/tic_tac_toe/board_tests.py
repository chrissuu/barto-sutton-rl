from board import Board, is_board

# tie test case
s1 = [['X','X','O'],
      ['O','O','X'],
      ['X','O','X']]
B1 = Board(s1)

assert(is_board(B1.state))
assert(B1.check_finished() == 'TIE')

# not a valid board test case (more O's than X's)
s2 = [[None, 'X','O'],
      ['O','O','X'],
      [None, 'O','O']]
B2 = Board(s2)

assert(not is_board(B2.state))

# left diagonal winner test case
s3 = [['X', 'X','O'],
      ['O', 'X','X'],
      ['O', 'O','X']]
B3 = Board(s3)

assert(is_board(B3.state, debug_prints=True))
assert(B3.check_finished() == 'X')

# right diagonal winner test case
s4 = [['O', 'X','X'],
      ['O', 'X','O'],
      ['X', 'O','X']]
B4 = Board(s4)

assert(is_board(B4.state))
assert(B4.check_finished() == 'X')


# not a valid board test case (two winners)
s5 = [['O', 'X','X'],
      ['O', 'O','X'],
      ['O', 'X','O']]
B5 = Board(s5)

assert(not is_board(B5.state))

# not a valid board test case (two winners)
s6 = [['O', 'X','X'],
      ['O', 'X','X'],
      ['O', 'X','O']]
B6 = Board(s6)

assert(not is_board(B6.state))

s8 = [['O','X','X'],
      ['O', None, 'X'],
      ['O','O','X']]

B8 = Board(s8)

assert(not is_board(B8.state, debug_prints=True))

s9 = [['X','O',None],
      ['X','O','X'],
      ['X','O','O']]

B9 = Board(s9)

assert(not is_board(B9.state, debug_prints=True))

s10 = [[None,'X',None],
      ['O','X','X'],
      ['O','X','O']]

B10 = Board(s10)

assert(is_board(B10.state, debug_prints=True))
print(B10.check_finished())
