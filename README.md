# MSCSAPPStatus
A python script to check MS CS admission results in batch without the pain of having to manually login to each website individually. 

Currently it supports the following universities:
+ Purdue
+ Arizona State 
+ Suny Stony Brook
+ Virginia Tech.
+ North Eastern
+ TAMU
+ UCSD, thanks to [marmikcfc](https://github.com/marmikcfc)

Python Requirements:
+ [Mechanize](https://pypi.python.org/pypi/mechanize/)

### Running Application

1.Just checking application status without any log. 
```python allCombined.py```

Sample Output:

```
Purdue Status : Under Review
----x----
ASU Status : In Review
----x----
SUNYSB Status : Submitted
----x----
vtech Status : In Review
----x----
NEU Status : Submitted
----x----
```

2.Application status with log.
```python allCombined.py 1```

Sample Output:

```
Purdue login in progress...
logged in successfully...
Purdue Status : Under Review
----x----
ASU login in progress...
logged in successfully...
ASU Status : In Review
----x----
SUNYSB login in progress...
logged in successfully...
SUNYSB Status : Submitted
----x----
vtech login in progress...
logged in successfully...
vtech Status : In Review
----x----
NEU login in progress...
logged in successfully...
NEU Status : Submitted
----x----
```

3.Application status with log + saving html of logged in webpage.
```python allCombined.py 2```

```
Purdue login in progress...
logged in successfully...
Purdue Status : Under Review
----x----
ASU login in progress...
logged in successfully...
ASU Status : In Review
----x----
SUNYSB login in progress...
logged in successfully...
SUNYSB Status : Submitted
----x----
vtech login in progress...
logged in successfully...
vtech Status : In Review
----x----
NEU login in progress...
logged in successfully...
NEU Status : Submitted
----x----
```

\+ html files generated.
