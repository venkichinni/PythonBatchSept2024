"""
Escape sequences
\n
\t
\b
"""

print("hello \tworld \tpython")

print("hello \tworld \npython")
print(r"hello \tworld \tpython")

print("C:\my\newfolder") 
print(r"C:\my\newfolder")
print()

print("hello") 
print("world")


print("hello", end="\n")
print("world", end="\n")

print("hello", end="____")
print("world",end="____")


print("hello", "python", 12132, end="\t") 
print("world") 

print("hello", "python", 12132, end="\t",sep=":") 
print("world") 

print(1, 2, 3, 4, 5, sep=";", end="\t")
print("a", "b", "c", "d", sep="-")


"""
-b
"""

print("hel\blo")
print("1234\b56")
print("\bsecond")
print("second\b")
print("second\b1")


print("hel\rlo")
print("1234567\rDOG")
print("13\rDOG")

"""
    unicode
"""
print("\u20B9")  
print("\u018e") 

# \x... - hexadecimal number
print("\x21")
print("\xf2")

print("\u0C4C")


print("#$%*&^(*;")
