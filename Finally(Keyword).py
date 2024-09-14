def myfunc():
    a=[1,5,2,4,7,8]
    try:
        ind=int(input("Enter the index of which value you want to see:"))
        print(f"Your value is {int(a[ind])}")
    except:
        print("You entered invalid index.")
    finally:
        print("I am always executed.")
myfunc()
