#Guess the number

i=0
mynum=18

while(i<5):
    num=int(input("Guess the number\n"))
    if num<mynum:
        print("You entered lesser number\n")


    elif num>mynum:
        print("You entered greater number\n")


    else:
        print("You won!!!\n")
        print("You guess in",i+1,"times\n")
        break
    i=i+1

if(i>=5):
    print("Game over......")








'''
n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1


if(number_of_guesses>9):
    print("Game Over")
'''