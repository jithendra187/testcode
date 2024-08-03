#!/usr/bin/python
firstnum = 0
secnum = 1
fibnum = 0
prevnum = 0
prevnum2 = 0
totalcount = 20
counter = 0

while (totalcount - counter)  > 0:
    if(counter == 0):
        print(firstnum, end = " ")
    elif(counter == 1):
        print(secnum, end = " ")
    else:
        fibnum = firstnum + secnum
        print(fibnum, end = " ")
        firstnum = secnum
        secnum = fibnum
    counter = counter + 1
    
