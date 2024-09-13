s1={1,5,3}
s2={7,3,9}
print(s1.intersection(s2))
#print(s1.intersection_update(s2))
print(s1)
print(s2)
print(s1.union(s2))
#print(s1.difference_update(s2))
print(s1.isdisjoint(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
for values in s1:
    print(values)

