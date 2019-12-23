def printTwocharDownward(symbol,n):
    ch='.'
    number_of_space=0
    number_of_character=n
    if n%2==0:
        total_no_of_line=int(n/2)
    else:
        total_no_of_line=int(n/2)+1

    count=1
    while count<=total_no_of_line:
        print(ch*number_of_space,symbol*number_of_character,ch*number_of_space)
        number_of_space +=1
        number_of_character -=2
        count +=1
    return
printTwocharDownward('*',6)
