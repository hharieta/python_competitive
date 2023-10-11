from sys import stdout

"""
Python code to apply a function on a list.
map takes as parameters the function named double_money
and the name of the list the function needs to be applied upon.
"""
income = [10, 30, 75]
 
def double_money(dollars):
    return dollars * 2
 
new_income = list(map(double_money, income))
stdout.write(new_income.__str__())