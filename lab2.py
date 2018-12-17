def new_list():
	a=[5,10,15,20]
	b=[]
	b.append(a[0])
	b.append(a[-1])
	print(b)
new_list()

a=[1,1,2,3,5,8,13,21,34,55,89]
def yay(a):
    y=[]
    x=int(input('enter a number'))
    for i in a :
        if i<x:
            y.append(i)
    print(y)
        
yay(a)

list1= [1,2,3,6,7,9,10,34,99,169]
list2= [1,2,4,7,9,36,99,100,169,200]
list3=[]
def common():
	for x in list1:
		for y in list2:
			if x==y:
				list3.append(x)


common()	
print(list3)		

c=0
input1= input("prime?")
for i in range(input1):
	if (input1%(i+1)==0):
		c=c+1

if(c==2):
	print("it is prime")
else:
	print("not prime")		