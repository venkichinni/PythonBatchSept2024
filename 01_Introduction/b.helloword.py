#!usr/bin/python3
"""
    shebang line
    https://peps.python.org/pep-0008/


"""

print("Hello world!")
print(True)
print(True, 123, None)


def wishes(name):
    wish="How are you {0}".format(name)
    print(wish)

wishes("venkat")