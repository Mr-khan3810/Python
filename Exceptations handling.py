a=input("Enter a number:")
ind={2,5,3}
try:
    print(f"The table of {a} is ")
    for i in range(1,11):
        print(f"{int(a)} * {i} ={int(a)*i}")
except:
    print("You enetred did not enter an integer.So,it doesn't have multiplication table.")
try:
    n=int(a)
    for i in range(1,int(a)):
        a=i*int(a)
    print(f"The factorial of the {n} is {int(a)}")
except:
    print("You enetred a string for factorial. So,it's factorial is not possible")
try:
    print(ind[0])
except:
    print("You entered invalid index")