import datetime
from sys import stdout

alphabets = [str(x) for x in range(1000000)]
a = datetime.datetime.now()
for item in alphabets:
    len(item)

b = datetime.datetime.now()
stdout.write(str((b-a).total_seconds())+'\n')

a = datetime.datetime.now()
fn = len
for item in alphabets:
    fn(item)

b = datetime.datetime.now()
stdout.write(str((b-a).total_seconds())+'\n')
