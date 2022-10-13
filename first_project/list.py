a=[3,2,7,9,6]
# even-mul5 , odd-mul2
# [10,14] -o/p

b=[]

for i in a:
    if i%3 == 0:
        continue
    elif i%2 == 0:
        b.append(i*5)
    else:
        b.append(i*2)
print(b)

