ida=[1,2,34,5,88,99]
b=[3,4,5,11,7]
c=[]
##for x in range(len(a)):
##    c.append(a[x]+b[x])
for i,j in zip(a,b):
    c.append(i+j)
print("Resultant list"+str(c))
