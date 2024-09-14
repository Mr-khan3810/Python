a=input("Enter your code which you want to decode:")
if(len(a)>2):
    b=a[3:len(a)-3]
    n=b[len(b)-1]
    b=b[0:len(b)-1]
    print(f"Your code after decoding is \"{n}{b}\"")
else:
    r=a[::-1]
    print(f"Your code after decoding is \"{r}\"")
