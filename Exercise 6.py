# Snake Water Gun

import random
print("##########SNAKE WATER GUN##########\n\n")
i=0
count=0
temp=0
while (i<10):
    lst = ["Snake","Water","Gun"]
    choice = random.choice(lst)
    print("Enter S for snake")
    print("Enter W for water")
    print("Enter G for gun\n\n")
    print("Snake,Water,Gun:",end=" ")
    ch = input()

    if ch=="S" and choice=="Snake":
        print("Your guess",ch,"and computer guess",choice)
        print("Tie\n")

    elif ch=="S" and choice=="Water":
        print("Your guess",ch,"and computer guess",choice)
        print("You lose\n")
        temp = temp +1
    elif ch=="S" and choice=="Gun":
        print("Yoor guess",ch,"and computer guess",choice)
        print("You lose\n")
        temp = temp + 1
    elif ch=="W" and choice=="Snake":
        print("Your guess",ch,"and computer guess",choice)
        print("Tou win\n")
        count = count + 1
    elif ch=="W" and choice=="Water":
        print("Your guess",ch,"and computer guess",choice)
        print("Tie\n")
    elif ch=="W" and choice=="Gun":
        print("Your guess",ch,"and computer guess",choice)
        print("You win\n")
        count = count + 1
    elif ch=="G" and choice=="Snake":
        print("Your guess",ch,"and computer guess",choice)
        print("You win\n")
        count = count + 1
    elif ch=="G" and choice=="Water":
        print("Your guess",ch,"and computer guess",choice)
        print("You lose\n")
        temp = temp + 1
    elif ch=="G" and choice=="Gun":
        print("Your guess",ch,"and computer guess",choice)
        print("Tie\n")
    else:
        print("\nTerminate")
        print("You entered wrong choice")
        break
    i = i + 1

print("\nYour score = ",count)
print("Computer score = ",temp)
if count>temp:
    print("YOU WON")
elif count<temp:
    print("COMPUTER WON")
else:
    print("Tie")




