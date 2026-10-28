#Indexing Basics

s="Python"
print(s[0],s[-1],s[6])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(s[0],s[-1],s[6])
IndexError: string index out of range


#s[6] raises an IndexError: string index out of range because valid indices for a 6-character string range from 0 to 5.


#Positive indexing starts from 0 at the left (beginning)and increases to the right.
#Negative indexing starts from -1 at the right (end)and decreases (moves leftwards).
s="Hello"
print(s[-2])
l

#Indexing:Accessing an out-of-range index (e.g., s[10]) raises an IndexError.
#Slicing out of range does not raise an error

s="Code"
print(s[1:10])
ode

s="Code"
print(s[10])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(s[10])
IndexError: string index out of range


s="mississippi"
# First 's'
print(s.index('s'))
2
# Last 's'
print(s.rindex('s'))
6


s="abcdef"
print(s[-1],s[-3],s[-6])
SyntaxError: multiple statements found while compiling a single statement

s = "abcdef"print(s[-1], s[-3], s[-6])
SyntaxError: invalid syntax


s="abcdef"

print(s[-1],s[-3],s[-6])
SyntaxError: multiple statements found while compiling a single statement



s="abcdef"
print(s[-1],s[-3],s[-6])
f d a

#Negative indexing starts from -1 at the right(end)of the string and decreases(moves leftwards).


#SLICING BASICS

#syntax for string slicing in Python
s[start:stop:step]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s[start:stop:step]
NameError: name 'start' is not defined
#s[start:stop:step]

#start: The starting index (inclusive)
#stop: The ending index (exclusive)
#Step: how many positions to move each time


s="HelloWorld"
print(s[0:5])
Hello
print(s[5:])
World
print(s[:5])
Hello
print(s[:])
HelloWorld



s="Python"
print(s[4:1])

#""(empty string)
#With a positive step (+1), Python expects the start index to move forward toward the stop index. Since it cannot move backwards, it returns an empty string without throwing an error.


#last 3 characters of a string using slicing, without knowing its length
print(s[-3:])
hon


s="abcdefgh"
print(s[::1])
abcdefgh
print(s[::2])
aceg
print(s[1::2])
bdfh


#STEP & REVERSE SLICING

#reverse a string using slicing

s="Python"
print(s[::-1])
nohtyP

s="abcdefgh"
print(s[::-1])
hgfedcba
#reverses the entire string
print(s[::-2])
hfdb
#reverses and skips every alternate letter
print(s[6:1:-1])
gfedc
#starts at index 6 ('g'), goes down to exclusive stop index 1 ('b')
 
 
s="a1b2c3d4e5"
print(s[1::3])
1c4
#extract every 3rd character from a string starting from index 1
 
 
s="Python"
print(s[5:0:-1])
nohty
print(s[5::-1])
nohtyP
print(s[:0:-1])
nohty
 
 
#start and stop values that exceed string boundaries with a negative step
 
s="hello"
print(s[100::-1])
olleh
print(s[::-100])
o
 
 
#INTERMEDIATE SLICING CHALLENGES
s="abcdefghij"
print(s[2:8])
cdefgh
 
 
#replace a portion of a string using slicing
s="Hello World"
ss=s[:6]+"Python"
print(ss)
Hello Python
 
