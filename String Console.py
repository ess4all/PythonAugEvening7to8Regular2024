Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = True
type(x)
<class 'bool'>
#String
x = 'hey'
type(x)
<class 'str'>
x = "Hey"
type(x)
<class 'str'>
x = '''Features:
1.Dynamically Typed Programming
2.Open  Source
3.High LEVEL
4.General Purpose
5.Interpreted Programming'''
print(x)
Features:
1.Dynamically Typed Programming
2.Open  Source
3.High LEVEL
4.General Purpose
5.Interpreted Programming
#multi line string
x = 'Python's syntax is very easy'
SyntaxError: unterminated string literal (detected at line 1)
x = "Python's syntax is very easy"
print(x)
Python's syntax is very easy
x = 'Python\'s syntax is very easy'#escape character
print(x)
Python's syntax is very easy
>>> x
"Python's syntax is very easy"
>>> x[-1]
'y'
>>> x[0]
'P'
>>> x[0:7]
"Python'"
>>> #python -ending - n-1
>>> x[:7]
"Python'"
>>> x[0:]
"Python's syntax is very easy"
>>> x[:]
"Python's syntax is very easy"
>>> x[0:11]
"Python's sy"
>>> x[0:11:1]
"Python's sy"
>>> x[0:11:2]
"Pto' y"
>>> #reverse
>>> x
"Python's syntax is very easy"
>>> x[::-1]
"ysae yrev si xatnys s'nohtyP"
