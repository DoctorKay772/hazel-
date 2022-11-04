tup = (1,2,3,4,8)

kup=list(tup)
kup[4] = 5
print(kup)
lst1 = [6,7,8,9,10]
kup.extend(lst1)
print(kup)
tup= tuple(kup)
print(tup)
