x=[1,2,3,4,'python',12.5,[8,7,9,10.5],[45,56,78.9,'ranjan','amit']]
def filterInt(a):
    temp=[]
    for i in a:
        if isinstance(i,int):
            temp.append(i)
    return temp
def filterFloat(a):
    temp=[]
    for i in a:
        if isinstance(i,float):
            temp.append(i)
    return temp
def filterString(a):
    temp=[]
    for i in a:
        if isinstance(i,str):
            temp.append(i)
    return temp
    
def filterList(a):
    tempstr=[]
    tempflt=[]
    tempint=[]
    
    for i in a:
        if isinstance(i,str):
            tempstr.append(i)
        elif isinstance(i,float):
            tempflt.append(i)
        elif isinstance(i,int):
            tempint.append(i)
        elif isinstance(i,list):
            
            tempint =tempint+filterInt(i)
            tempstr=tempstr+filterString(i)
            tempflt=tempflt+filterFloat(i)
            
    return(tempstr,tempflt,tempint)
p,q,r=filterList(x)
print("String",p)
print("Float",q)
print("Int",r)

            
            
