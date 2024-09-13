dic={
    101: "ALI",
    102: "Ahmad",
    103: "C",
    104: "D"
}
dic1={
    111:67,
    112:56,
    118:34
}
print(dic[101])
print(dic.get(105))#It will find the 105 if not found print "None"
print(dic.keys())
print(dic.values())
for key in dic.keys():#Here "Keys" is a keyword used for index in dictionary.
    print(dic[key])
# for key in dic.keys():
    # print(f"The key corresponding {key} is {dic[keys]}")
for key, value in dic.items():
    print(f"The key corresponding {key} is {value}")
dic.update(dic1)
print(dic)
print(dic.pop(118))
# print(dic.clear())
print(dic.popitem())
del dic[111]
print(dic)