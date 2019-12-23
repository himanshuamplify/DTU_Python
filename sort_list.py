lst=[['Ankit',10],['ZChawan',11],['Ravi',5]]
##l=len(listsort)
##for x in range(len(listsort)):
##    for y in range(l-x-1):
##        if(listsort[y][1] > listsort[y+1][1]):
##            temp=listsort[y]
##            listsort[y]=listsort[y+1]
##            listsort[y+1]=temp
##print(listsort)
print(lst)
lst.sort(key=lambda a:a[0],reverse=True)
print(lst)

lst.sort(key=lambda a:a[1],reverse=False)
print(lst)

lst.sort(key=lambda a:a[1],reverse=True)
print(lst)
