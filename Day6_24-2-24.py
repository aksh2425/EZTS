#p1--super method usage
'''class parent:
    def __init__(self):
        print("parent method ")
class child(parent):
    def __init__(self):
        super().__init__()
        super()
        print("child method")
c=child()'''
#p2-single inheritance
'''
class DOb:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def display1(self):
        d={1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun",7:"jul",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}
        print(self.date):
        print(d[self.month])
        print(self.year)
class details(DOb):
    def __init__(self,name,age,date, month,year):
        self.name=name
        self.age=age
        self.date=date
        self.month=month
        self.year=year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)
p=details("aksh",20,23,3,2003)
p.display()
p.display1()'''
#MULTILEVEL INHERITANCE
'''class parent:
    def func1(self):
        print("fun1")
class child(parent):
    def func2(self):
        print("func2")
class child2(child):
    def func3(self):
        print("this is func")
ob=child2()
ob.func1()
ob.func2()
ob.func3()'''
#mutli level
'''
class vehicle:
    def __init__(self,fueltype):
        self.fueltype=fueltype
    def display3(self):
        print(self.fueltype)
class motor(vehicle):
    def __init__(self,fueltype,cc):
        self.fueltype=fueltype
        self.cc=cc
    def display2(self):
        print(self.fueltype)
        print(self.cc)
class car(motor): 
    def __init__(self,name,fueltype,cc):
            self.fueltype=fueltype
            self.name=name
            self.cc=cc
    def display1(self):
            print(self.fueltype)
            print(self.cc)
            print(self.name)
v1 =car("BMW","petrol","cc")
v1.display1()
v1.display2()
v1.display3()'''
#hierarchical inheritance
'''class shape:
    def area(self):
        print("hi")
class rectangle(shape):
    def __init__(self,leen,b):
        self.leen=leen
        self.b=b
    def area(self):
        print(self.leen*self.b)
class square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)
c=square(5)
c.area()
c1=rectangle(4,9)
c1.area()
o=shape()
o.area()'''
#abstraction
'''from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        print("hi")
class rectangle(shape):
    def __init__(self,leen,b):
        self.leen=leen
        self.b=b
    def area(self):
        print(self.leen*self.b)
class square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)
c=square(5)
c.area()
c1=rectangle(4,9)
c1.area()
o=shape()
o.area()'''
#exception handling
try:
    a=int(input())
    c=2//a
except ZeroDivisionError:
    print("division error")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("hello")