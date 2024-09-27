#!usr/bin/python3
### simple intrest caliculator





## input feilds


principal=float(input("Enter initial principal bal amount (P) : "))

rate=float(input("Enter Annual intrest rate(r). please enter in decimals ex: 0.06 for 6% :"))

time = float(input("enter time in years (t) : "))

### Final Amount = P(1+(rt))

final_amount = principal * (1 + (rate * time))


print (" the final amount for " + str(time) + "years will be :", final_amount)





##### compound intrest. A=P(1+ (r/n))**nt

times_compounded = int(input("Enter the number of times interest is compounded per year: "))


final_amount=round(principal * (1 + rate / times_compounded) ** (times_compounded * time),2)


print (" the final amount for compound intrest  " + str(time) + "years will be :", final_amount)
