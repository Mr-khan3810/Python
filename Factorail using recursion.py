def factorial(a):
    if(a==1 || a==0 ):
        return 1
    else:
        return (int(a)*factorial(int(a-1)))
a=input("Enter the number:")
print(factorial(int(a)))