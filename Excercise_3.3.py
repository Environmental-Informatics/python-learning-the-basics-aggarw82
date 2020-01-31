""" Printing Grids

Implementation of Exercise 3.3 Part 1 through 2
Book: Think Python 2nd Edition by Allen B. Downey
Edition: 2e
Link: https://greenteapress.com/wp/think-python-2e/
"""

# call function 'f' twice and print 'end_char' to end line
def do_twice(f, end_char):
    f()
    f()
    print(end_char)

# call function 'f' four times and print 'end_char' to end line
def do_four(f, end_char):
    f()
    f()
    f()
    f()
    print(end_char)

# print '|        '
def print_st_line():
    print('|        ',end=' ')

# print '+ - - - -'
def print_plus_row():
    print('+ - - - -',end=' ')

# print only 1 row of grid
def one_row(f):
    f(print_plus_row, '+')
    f(print_st_line, '|')
    f(print_st_line, '|')
    f(print_st_line, '|')
    f(print_st_line, '|')



# print 2 rows for 2x2 grid
print('Grid: 2x2 \n')
one_row(do_twice)
one_row(do_twice)
do_twice(print_plus_row, '+')

# print 4 rows for 4x4 grid
print('\n\n\n Grid: 4x4 \n')
one_row(do_four)
one_row(do_four)
one_row(do_four)
one_row(do_four)
do_four(print_plus_row, '+')



"""
Author: Varun Aggarwal
Username: aggarw82
Github: https://github.com/Environmental-Informatics/python-learning-the-basics-aggarw82
"""