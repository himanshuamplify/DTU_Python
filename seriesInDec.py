def printSeriesIncreasing1(symbol,n):
    count=1
    while count<=n:
        print(symbol*count)
        count =count +1
    return

def printSeriesDecreasing1(symbol,n):
    count=n
    while count>=1:
        print(symbol*count)
        count =count -1
    return
def printSeriesIncDec1(symbol,n):
    if n%2==0:
        printSeriesIncreasing1(symbol,int(n/2))
        printSeriesDecreasing1(symbol,int(n/2))
    elif n%2 ==1:
        printSeriesIncreasing1(symbol,(int(n/2)+1))
        printSeriesDecreasing1(symbol,int(n/2))
    return
printSeriesIncDec1('*',4)
