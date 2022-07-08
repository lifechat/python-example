

a = {'x':1,'z':3}
b = {'y':2, 'z':4}

data = ['ACME',50,91.1,(2012,12,21)]


name,shares,prices,date = data;


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
# name,email,*phone_numbers = record;
name,*_,(year,*_) = data

print(name,year)


def foo(x,y):
    print('foo',x,y)

def bar(s):
    print('bar',s)


for tag,*args in records:
    if tag == 'foo':
        foo(*args)
    elif tag == 'bar':
        bar(*args)


print(name,shares,prices,date)
from collections import ChainMap

c = ChainMap(a,b);

print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)



### 8。7 调用父类方法


class A:
    def spam(self):
        print("A.spam")

class B(A):
    def spam(self):
        print("B.spam")
        super().spam() # 回调父方法