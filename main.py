class parent:
    def sum(self,a,b):
        return a+b
class your_class:
    def Fun(self,a,b):
        self.a=a
        self.b=b
        '''
        we can call method of another class
        by using their class name and function with dot operator.
        '''
        x=parent.sum(self,a,b)
        print("sum=",x)
#class object of child class or
ob=your_class()
x=int(input("enter 1st no."))
y=int(input("enter 2nd no."))
#fuction call of your class
ob.Fun(x,y)

'''================other class call another method of other class================'''

class A:
    def add_f(self, a, b):
     return a+b

class B:
    def sum_f(self, a, b, c):
     d=A().add_f(a, b)
     print(d+c) #A().add_f(a, b) + c
     print("hello , changes after commit")


b=B()
x=int(input("enter 1st no."))
y=int(input("enter 2nd no."))
z=int(input("enter 2nd no."))
#fuction call of your class
#b.Fun(x,y)
b.sum_f(x, y, z)

