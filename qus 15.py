def exponent(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*exponent(base,exp-1))
base=int(input("Enter base:"))
exp=int(input("Enter exponential: "))
print(exponent(base,exp))