from sys import stdout

"""
Concatenation of list of strings:
bad implementation (new string will be created in each loop):

string = ""
lst = ["Geeks", "for", "Geeks"]
for i in lst:
    string += i
print(string

"""
lst = ["Geeks", "for", "Geeks"]
string = ''.join(lst)
stdout.write(string)
