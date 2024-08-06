Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String
x = "Hello how are you Doing??"
x.lower()
'hello how are you doing??'
x.upper()
'HELLO HOW ARE YOU DOING??'
x.swapcase()
'hELLO HOW ARE YOU dOING??'
#String - immutable
]
x
'Hello how are you Doing??'
len(x)
25
x.title()
'Hello How Are You Doing??'
x
'Hello how are you Doing??'
x.find("o")#it will return first occuring char's index
4
x.rfind("o")
19
x.find("o",0)
4
x.find("o",5)
7
x.index("o",5)
7
x.find("X")
-1
#-1 means substring not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x.index("X")
ValueError: substring not found

x
'Hello how are you Doing??'
x.find("how")
6
x.find("hxqwe")
-1
x
'Hello how are you Doing??'

================ RESTART: /Users/sahilkumar/Documents/webbrowser1.py ===============
enter msgopen google
x = "open google"
x[5:]
'google'

x
'open google'
x.split()
['open', 'google']
x.split()[0]
'open'
x.split()[-1]
'google'

================ RESTART: /Users/sahilkumar/Documents/webbrowser1.py ===============
enter msgopen twitter

================ RESTART: /Users/sahilkumar/Documents/webbrowser1.py ===============
enter msgopen twitter

================ RESTART: /Users/sahilkumar/Documents/webbrowser1.py ===============
enter msgopen youtube

================ RESTART: /Users/sahilkumar/Documents/webbrowser1.py ===============
enter msg
Traceback (most recent call last):
  File "/Users/sahilkumar/Documents/webbrowser1.py", line 3, in <module>
    msg = input("enter msg")
KeyboardInterrupt

x
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = "hello Python"
x.startswith("h")
True
x.endswith("e")
False
"e" in x#in - membership  operator
True
x = "hello Python"
x.split("o")
['hell', ' Pyth', 'n']
x.split()
['hello', 'Python']
z = x.split()
z
['hello', 'Python']
" ".join(z)
'hello Python'
"#".join(z)
'hello#Python'
x
'hello Python'
x*3
'hello Pythonhello Pythonhello Python'
x = "hello"
y = "python"
x+y
'hellopython'
>>> x="sahil"
>>> x.center(6)
'sahil '
>>> x.center(20)
'       sahil        '
>>> x.center(20,"*")
'*******sahil********'
>>> x = x.center(20,"*")
>>> x
'*******sahil********'
>>> x.lstrip("*")
'sahil********'
>>> x.rstrip("*")
'*******sahil'
>>> x.strip("*")
'sahil'
>>> 'google'
'google'
>>> x =12
>>> x = x+1
>>> x
13
>>> 
>>> x+=1
>>> x
14
>>> x -= 10
>>> x
4
