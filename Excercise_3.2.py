""" Calling function from a function

Implementation of Exercise 3.2 Part 1 through 4 
Book: Think Python 2nd Edition by Allen B. Downey
Edition: 2e
Link: https://greenteapress.com/wp/think-python-2e/
"""

# call function 'f' with argument 'value'
def do_twice(f, value):
	f(value)
	f(value)

# print argument 'Bruce' twice
def print_twice(bruce):
	print(bruce)
	print(bruce)


# call function 'do_twice'
do_twice(print_twice, 'Spam')	


"""
Author: Varun Aggarwal
Username: aggarw82
Github: https://github.com/Environmental-Informatics/python-learning-the-basics-aggarw82/lab01
"""