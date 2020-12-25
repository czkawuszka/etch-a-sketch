#Etch-a-sketch by czkawuszka uwu
import numpy as np
print("Hello to etch-a-sketch!")
print(" ")
print("Creating table...")
print(" ")


len=50

cord = [['-' for x in range(len)] for y in range(20)]

print("Table finished!")


posy, posx = 0, 0
cord[posy][posx]='o'
painting='n'
erasing='n'
temp2='-'
while True:
    y=0
    x=0
    while(y<20):
        while(x<len):
            print(cord[y][x], end='')
            x+=1
        x=0
        y+=1
        print(" ")

    p_input=str(input('Command: '))
    if(p_input=='up' or p_input=='u'):
        print('up')
        if(posy==0):
            print("You're already at the top end of the space")
        else:
            posy-=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy+1][posx]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
            elif(temp=='#' and erasing=='y'):
                temp2='-'
            else:
                temp2=temp
    elif(p_input=='down' or p_input=='d'):
        print('down')
        if(posy==19):
            print("You're already at the bottom end of the space")
        else:
            posy+=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy-1][posx]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
            elif(temp=='#' and erasing=='y'):
                temp2='-'
            else:
                temp2=temp
    elif(p_input=='left' or p_input=='l'):
        print('left')
        if(posx==0):
            print("You're already at the left end of the space")
        else:
            posx-=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy][posx+1]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
            elif(temp=='#' and erasing=='y'):
                temp2='-'
            else:
                temp2=temp
    elif(p_input=='right' or p_input=='r'):
        print('right')
        if(posx==49):
            print("You're already at the right end of the space")
        else:
            posx+=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy][posx-1]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
            elif(temp=='#' and erasing=='y'):
                temp2='-'
            else:
                temp2=temp
    elif(p_input=='pos'):
        print('y= '+str(posy)+' x= '+str(posx))
    elif(p_input=='exit'):
        break
    elif(p_input=='paint'):
        painting='y'
        temp2='#'
    elif(p_input=='stop'):
        painting='n'
        erasing='n'
    elif(p_input=='erase'):
        erasing='y'
        temp2='-'
    else:
        print("Wrong input!")
