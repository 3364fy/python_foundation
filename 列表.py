lst1=['hello','world',98,425,22,43,524,5,98]
lst2=list(['hello','world',98])
print(lst1)
print(lst2)
print(lst1[0])
print(lst2[-1])
print(lst1.index(98))
print(lst1.index(98,3,9))
print(lst1[0:3:1])
print(lst1[0:3])
print(lst1[0:3:])
print(lst1[:3:1])
print(lst1[0::1])
print(lst1[::-1])
print(lst1[3:0:-1])
print('w'in lst1)
for a in lst1:
    print(a)
