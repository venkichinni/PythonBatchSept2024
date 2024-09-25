#!usr/bin/python3

"""
Print()
"""

name="python" #str
print(name)

print("name is : ",name)

print("name of the student is :", name)
print("name of the student is :" + name)

print("name of the student is :", name,sep="-")

print(1, 2, 3, 4, 5, 6)  # default sep=' '
print(1, 2, 3, 4, 5, 6, sep="")
print(1, 2, 3, 4, 5, 6, sep="~")


# NOTE: Python is dynamic typed language
name = 1232
print("Name of Student is", name)

print("1+2 :", 1+2)
print("'1'+'2' :", "1"+"2")

print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")

print("int('234')   =", int("234"))



print("Name of Student is" + str(name))
print("Name of Student is" + " " + str(name))