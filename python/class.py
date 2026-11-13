class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
"""a=int(input("enter length"))
b=int(input("enter breadth"))
rec=rectangle(a,b)
#print(rec.area())"""

#inheritance property
class square(rectangle):
    pass
squa=square(length=int(input("enter 1")),breadth=int(input("enter 2")))
print(squa.area())
