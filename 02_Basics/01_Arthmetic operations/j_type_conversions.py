
"""
Data Type Conversions
- int, float, complex, boolean, string, None

    int - decimal       - int() -base 10  (0-9)
        - binary        - bin() -base  2  (0-1)
        - hexadecimal   - hex()
        - octal         - oct()
    float
        float()
    String
        str()


int -> float
int -> str

float -> int
float -> str

str  -> int
str -> float

"""

num = 12
print("num=", num, type(num))

# int -> float
print(12, float(12))  # 12 12.0

# int -> str
print(12, str(12))

# float. -> Int
print(3.14, int(3.14))

# Str -> int
print(3.1416, str(3.1416))


# str  -> int
print("23",  int("23"))  # '23 ', 23 
print("23 ", int("23 "))  # '23 ', 23

# str -> float
print("23   ", float("23"))     # '23   ', 23.0
print("23.24", float("23.24"))  # '23.24', 23.24
print("23.  ", float("23."))    # '23.  ', 23.0

print(int())
print(bool())
print(float())
print(str())


print(float())                 # 0.0
print(float("+1.23"))         # 1.23
print(float("   -12345\n"))    # -12345.0
print(float("1e-003"))         # 0.001
print(float("+1E6"))           # 1000000.0
print(float("-Infinity"))      # -inf


print("str(12)          ", str(12))
print("str(121233.12323)", str(121233.12323))
print("str(-0.000012)   ", str(-0.000012))
print("str(True)        ", str(True))
print("str(None)        ", str(None))

num1 = 33
print("num1 =", num1, type(num1))  # -> Decimal form


# decimal -> binary form
print(23, bin(23), type(bin(23)))
print(23.24, bin(int(23.24)))  # 23.24, '0b10111'
print("bin(9)", bin(9))  # '0b1001'


# binary -> decimal form
print("0b1001", int("0b1001", base=0))  # 9
print("1001  ", int("1001", base=0))    # 1001
print("bin(9)", int(bin(9), base=0))    # 9

print((9).bit_length())
print((23).bit_length())
print((45).bit_length())


# Octal -> 0-7
# decimal -> octal
print("oct(9)  ", oct(9))  # '0o11'
print("oct(-23)", oct(-23))  # '-0o27'


# octal -> decimal
print(int(oct(9), base=8))  # 9
print(int("0o11", base=8))  # 9
print(int("11", base=8))    # 9
print(int("11"))  # 11


# decimal -> hexadecimal
print("hex(9)  ", hex(9))  # '0x9'
print("hex(-23)", hex(-23))  # '-0x17'

# hexadecimal -> decimal
print(int(hex(-23), base=16))  # -23
print(int("-0x17", base=16))  # -23
print(int("-17", base=16))  # -23
print(int("-17"))  # -17

# is_integer -> Return True if the float is an integer.
print((-2.0).is_integer())      # True
print((-2.1).is_integer())      # False
print((-1.9999).is_integer())   # False