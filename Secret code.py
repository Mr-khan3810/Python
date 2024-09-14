a=input("Enter a string:")
if(len(a)>=3):
    n=a[0]
    b=a[1:]
    print(f"Your encrypted code is \"asd{b}{n}mnb\"")
else:
    r=a[::-1]
    print(f"Your encrypted code is \"{r}\"")
