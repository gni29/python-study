'''


f2 = open("./test.txt",'r')
print(f2.read())
f2.close()

f3 = open("./test.txt",'a')
print(f3.write("Hello World222 \n"))
f3.close
'''
f = open("./test.txt",'r')
print(f.readline(), end=" ")
print(f.readline(), end= " ")
print(f.readline(), end = " ")
f.close()
