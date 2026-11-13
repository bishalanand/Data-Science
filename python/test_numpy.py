import numpy as ab
"""a=ab.array([1,2,3,5],dtype=float)
print(a)
print(type(a))"""
#for 2d array
"""b=ab.array([[[1,2,3],[4,5,6]],[[2,3,6],[7,5,6]]],dtype=float)
print(f"{b} \n {b.shape} \n {type(b)} \n {len(b)}")
print(b.ndim)
print(b[1,1,1])->to access element b[1,1,1] returns 5
print(b[1,:,:])"""
#creating array which consist of 0,1
"""c=ab.zeros([2,3])
print(c)
d=ab.ones([2,3],dtype=str)
print(d)
e=ab.full([3,4],34)#creates array of 3*4 in which every element is 34
print(e)
f=ab.random.randint(-4,1,size=(3,4))
print(f)
g=ab.identity(5,dtype=int)
print(g)"""
#performing aariithmetic operation on array
"""a=a+2
a=a*2
a=a**2"""#this will perform arithmetic operation with all element in a
#taking input from user to create array
d=input("enter the number")
data=list(map(float,d.split(",")))
c=ab.asarray(data,dtype=float)
print(c)