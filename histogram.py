Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>
import sys
import string

lines = sys.stadin.readlines()
total = 0
for line in lines:
    line = line.split()
    total+=int(line[1])
    print (line)

print(total)
    
for line in lines:
    line = line.split()
    word = line[0]
    count = int(line[1])
    per = int(count/total)*100

    print(word,'\t\t[', end='')
    print(((per+4)//5)*"*", end='')
    print('] ', per, "%", sep='')
