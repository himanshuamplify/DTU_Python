## Program for finding numbers in range which are divisible of 7 and not multiple of 5

l = []
for i in range(2000,3201):
    if(i%7==0) and (i%5!=0):
        l.append(str(i))

##print ','.join(l)


##------------------------------------------------##

## Find Factorial of a Program using function
def fact(x):
        if x==0:
            return 1;
        return x * fact(x-1)
##print("Enter the number to find factorial")
##x = int(raw_input())
##print fact(x)


##------------------------------------------------##

## WAP to create dictionary using (i:i*i)
##print("enter the number to find dictionary")
##n = int(raw_input())
##d = dict()
##for i in range (1,n+1):
##    d[i] = i*i

##print d

##------------------------------------------------##

##  WAP to create list and tuple from series of numbers entered by user
##values = raw_input()
##l = values.split(",")
##t = tuple(l)
##print l
##print t

##------------------------------------------------##
## WAP to create a class in python which accepts user input and print it in upper case


class InputOutputString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        print("enter your name buddy")
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

##strObj = InputOutputString()
##strObj.getString()
##strObj.printString()

##------------------------------------------------##

## WAP to accept the user input string from user and sort it alphabetically
##print("Enter the series of String with ',' as seperator")
##items = [x for x in raw_input().split(',')]
##items.sort()
##print ','.join(items)


##------------------------------------------------##
## WAP to accept user string input in two lines and print the combine name in capital Letters

lines =  []
#while True:
#    s = raw_input()
#    if s:
#        lines.append(s.upper())
#    else:
#        break;

#for sentence in lines:
#    print sentence
            
##------------------------------------------------##

## WAP to accept input from user using white spaces and print the words after removing all duplicate words and sort
#print("Enter your inout with spaces and duplicate words")
#s = raw_input()
#words = [word for word in s.split(" ")]
#print " ".join(sorted(list(set(words))))

##------------------------------------------------##

## WAP to find out all the numbers with all even digits between range 1000 and 3000
#values = []
#for i in range(1000,3000):
#    s = str(i)
#    if(int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#        values.append(s)
#print ",".join(values)

##------------------------------------------------##

## WAP that accepts sentence and calculates number of letters and digits

s = raw_input()
d = {"DIGITS":0,"LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS",d["LETTERS"]
print "DIGITS", d["DIGITS"]

##------------------------------------------------##

## WAP to accept password from user which should have
## 1 character of (a-z), 1 of (A-Z), 1 Number, 1 special symbol, min length 6, max length 12

import re
print("Enter your Passwords in ',' series")
value = []
items = [x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif not re.search("[\s]",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)

##------------------------------------------------##
## WAP to checkk the balance of  Deposit and withdrawl amount given by customer
print("Enter input as D 233 or W 433")
balance = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        balance+=amount
    elif operation=="W":
        balance-=amount
    else:
        pass
print balance
