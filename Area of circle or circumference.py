def circum(a):
    return float((2*3.14*float(a)))
def area(r):
    return float(3.14*float(r)*float(r))
ch=input("Enter choice:")
r=input("Enter radius:")
match(int(ch)):
    case 1:
        print("The area of circle is :",area(r))
    case 2:
        print("The circumference of circle is :",circum(r))
