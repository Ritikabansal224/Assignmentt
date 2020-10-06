l1 = [2,5,8,12,4,6,87,32,65]
l2 = [1,6,3,90,4,5,32,4]
l3 = ([n for n in l1 if n%2] + [n for n in l2 if not n%2])
print(l3)
