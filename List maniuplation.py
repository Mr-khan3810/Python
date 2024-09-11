l=[3,4,5,5,"Ali",True]
print(l)
print(type(l))
print(len(l))
print(l[0:5])
print(l[:-3])
li=[i*i for i in range(5)]
print(li)
print(l.index(5))
m=[0,1,2,11,7,45,33]
print(l.extend(m))
k=m+l
print(k)
print(m.sort())
print(m.append(7))
k[0]=54
print(k)
print(l.count(5))
print(m.reverse())
if "Ali" in l:
    print("Yes")
else:
    print("No")
if "Al" in "Ali":
    print("Yes")
else:
    print("No")
