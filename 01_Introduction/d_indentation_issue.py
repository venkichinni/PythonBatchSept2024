#!usr/bin/python3

print("hello world1!")

print("hello world3!")



if 12 > 3:
    print('12 is greater than 3')


if 12 > 34:
    print("greater")
else:
    print("It is lesser")



if 1 < 2:
    print("case 1")
elif 2 > 1:
    print("case 2")
else:
    print("case 3")



if 1 < 2:
    if 2 < 3:
        if 3 < 4:
            if 4 < 5:
                print("LESSER")
            else:
                print("something")
        else:
            print("something")
    else:
        print("something")



for i in range(9):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, "*", j, "=", i * j)
        j += 1
    print()
    i += 1



while i<10:
    j=0
    while j<10:
        print(i,"*",j,"=", i*j)
        j+=1
    print()
    i+=1

    




