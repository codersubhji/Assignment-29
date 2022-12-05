"""7. Write a Python script to count the number of Python keywords occurring in a python
source file."""
import keyword

ff=open("keyword.txt",'w')
l1=keyword.kwlist
l2=str(l1)
(ff.write(l2))
print("list successful created.")
ff.close()

count=1
for i in l1:
    print(count ,":",i)
    count+=1
ff.close()    
    