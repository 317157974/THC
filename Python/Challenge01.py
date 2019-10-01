Python 3.7.3 (default, Mar 27 2019, 13:36:35) 
[GCC 9.0.1 20190227 (Red Hat 9.0.1-0.8)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: /home/thc/THC/Python/Secuencias.py ================
M
E
27
>>> 
================ RESTART: /home/thc/THC/Python/Secuencias.py ================
M
<class 'str'>
E
<class 'str'>
27
<class 'int'>
>>> L1 = ["M", "E", 27]
>>> print(type(L1))
<class 'list'>
>>> 
================ RESTART: /home/thc/THC/Python/Secuencias.py ================
M
<class 'str'>
E
<class 'str'>
27
<class 'int'>
<class 'list'>
>>> print(t1)
('M', 'E', 27)
>>> print(t1[0])
M
>>> L1[3] = "L"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    L1[3] = "L"
IndexError: list assignment index out of range
>>> L1.
SyntaxError: invalid syntax
>>> L1.("L")
SyntaxError: invalid syntax
>>> L1.append("L")
>>> print(L1)
['M', 'E', 27, 'L']
>>> D6 = ["E", "M", "H" "T", "I", "W", "E", "I", "D"]
>>> print(D6)
['E', 'M', 'HT', 'I', 'W', 'E', 'I', 'D']
>>> D6.remove("HT")
>>> print(D6)
['E', 'M', 'I', 'W', 'E', 'I', 'D']
>>> D6.pop("I")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    D6.pop("I")
TypeError: 'str' object cannot be interpreted as an integer
>>> D6.pop("I")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    D6.pop("I")
TypeError: 'str' object cannot be interpreted as an integer
>>> D6.pop("T")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    D6.pop("T")
TypeError: 'str' object cannot be interpreted as an integer
>>> D6.count(D6)
0
>>> D6.count(list)
0
>>> D6.count.__sizeof__(D6)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    D6.count.__sizeof__(D6)
TypeError: __sizeof__() takes no arguments (1 given)
>>> D6.count.__sizeof__
<built-in method __sizeof__ of builtin_function_or_method object at 0x7f6db9171558>
>>> D6.count
<built-in method count of list object at 0x7f6db71ee308>
>>> D6.count.__class__
<class 'builtin_function_or_method'>
>>> D6.count.__class__(list)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    D6.count.__class__(list)
TypeError: cannot create 'builtin_function_or_method' instances
>>> 
================ RESTART: /home/thc/THC/Python/Secuencias.py ================
M
<class 'str'>
E
<class 'str'>
27
<class 'int'>
<class 'list'>
Traceback (most recent call last):
  File "/home/thc/THC/Python/Secuencias.py", line 8, in <module>
    L1[3] = "L"
IndexError: list assignment index out of range
>>> 
================ RESTART: /home/thc/THC/Python/Secuencias.py ================
M
<class 'str'>
E
<class 'str'>
27
<class 'int'>
<class 'list'>
Traceback (most recent call last):
  File "/home/thc/THC/Python/Secuencias.py", line 8, in <module>
    L1[3] = "L"
IndexError: list assignment index out of range
>>> 
================ RESTART: /home/thc/THC/Python/Secuencias.py ================
R
<class 'str'>
7
<class 'int'>
0
<class 'int'>
7
<class 'int'>
2
<class 'int'>
U
<class 'str'>
8
<class 'int'>
J
<class 'str'>
W
<class 'str'>
3
<class 'int'>
>>> 
