a=1
print(a)
a=2.0
print(a)
d="Nupur"
print(d)
'''
e=d+a
Traceback (most recent call last):
  File "/Users/nupursikka/Documents/Learn Python/typeCasting.py", line 8, in <module>
    e=d+a
      ~^~
TypeError: can only concatenate str (not "float") to str
print(e)
'''
e=d+str(a)
print(e)
