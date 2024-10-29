x=int(input("Enter a number : "))
a=0
b=1
print(a)
print(b)
for i in range (x):
    #add 
    c=a+b
    #after adding and printing should refresh variables by shift nbrs b will be a 
    a=b
    b=c
    print(c)