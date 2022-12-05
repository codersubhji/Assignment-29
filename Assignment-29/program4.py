#4. Write a Python script to store a list of city names in a file ‘cities.txt’

f=open("cities.txt",'w')
f.write("city name")

c2="\nIn this city is very beautifull and trust me if you try to understand then realy it's very amzg"
f=open("cities.txt",'a')
call=input("Enter your city name:")
print(call)
f.write(c2)
print(c2)

print("city name successfully printed")
f.close()

