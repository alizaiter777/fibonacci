nbr=int(input("Enter a number : "))
a=0
b=1
print(a)
print(b)
for i in range (nbr):
    #add 
    c=a+b
    #after adding and printing should refresh variables by shift nbrs a will take value of b and b will take value of c 
    a=b
    b=c
    print(c)
    print(c)

