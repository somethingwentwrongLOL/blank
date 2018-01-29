
import random #the import is used so that the random command can be initiated
count=0 #this is to make sure we start from 0
while count<=100: #with this we set the maximum limit to 100
    roll=input("press r to roll a dice") #this tells us what to do, what button to press to roll the dice
    if roll=='r': #this makes the r key the key used to roll the dice
        r=random.randint(1,6) #range of random shuffle
        count=count+r #kind of like a formula in which the count the previous value and r is the no. in the dice
        print("r is",r) #this tells us what no. has rolled up
        print("count is",count) #this tells us what our final value is..on which block we should be on
        input ("Press any key to exit") #used to ensure that the command doesn't exit the loop on its own
        if count==8: # the game begins
            count=37
            print("you've climbed the ladder to 37")
            print("your count is",count)

        if count==11: # same procedure is followed everywhere
            count=2
            print("you've been bitten by the snake go to 3")
            print("your count is",count)
        if count==25:
            count=4
            print("you've been bitten by the snake go to 4")
            print("your count is",count)
        if count==38:
            count=9
            print("you've been bitten by the snake go to 9")
            print("your count is",count)
        if count==40:
            count=68
            print("you've climbed the ladder to 68")
            print("your count is",count)
        if count==52:
            count=81
            print("you've climbed the ladder to 81")
            print("your count is",count)
        if count==65:
            count=46
            print("you've been bitten by the snakeg go to 37")
            print("your count is",count)
        if count==76:
            count=97
            print("you've climbed the ladder to 97")
            print("your count is",count)
        if count==89:
            count=70
            print("you've been bitten by the snake go to 37")
            print("your count is",count)
        if count==93:
            count=64
            print("you've been bitten by the snake go to 37")
            print("your count is",count)
        if count==100:
            count=100
            print("you've won the game..Congratulations") # the ending line
            print("your count is",count)    


















            
