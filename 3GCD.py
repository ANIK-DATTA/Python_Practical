a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

i = 1
while(i <= a and i <=b):
    if(a%i == 0 and b%i == 0):
        gcd = i
    i = i+1 

print("\n HCF of {0} and {1} = {2}".format(a,b,gcd))