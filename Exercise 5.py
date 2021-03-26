
#HEALTH MANAGEMENT SYSTEM



def gettime():
    import datetime
    return datetime.datetime.now()


def take(k):
    if k==1:
        print("Enter ::")
        print("\t  1.Exercise")
        print("\t  2.Food")
        c = int(input())
        if c==1:
            value=input("Type here\n")
            f=open("RohanExercise.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
            f.close()
        elif c==2:
            value = input("Type here\n")
            f=open("RohanFood.txt","a")
            f.write(str([str(gettime())])+": " + value + "\n")
            print("Successfully written")
            f.close()
    elif k==2:
        if c==1:
            value=input("Type here\n")
            f = open("HarryExercise.txt", "a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
            f.close()
        elif c==2:
            value = input("Type here\n")
            f = open("HarryFood.txt", "a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
            f.close()
    elif k==3:
        print("Enter ::")
        print("\t  1.Exercise")
        print("\t  2.Food")
        c = int(input())
        if c==1:
            value = input("Type here\n")
            f = open("HammadExercise.txt", "a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
            f.close()
        elif c==2:
            value = input("Type here\n")
            f = open("HammadFood.txt", "a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
            f.close()
    else:
        print("Please enter valid input::")
        print("1.Rohan")
        print("2.Harry")
        print("2.Hammad")


def retrieve(k):
    if k==1:
        print("Enter ::")
        print("\t  1.Exercise")
        print("\t  2.Food")
        c = int(input())
        if c==1:
            f = open("RohanExercise.txt")
            for i in f:
                print(i, end="")
            f.close()
        elif c==2:
            f = open("RohanFood.txt")
            for i in f:
                print(i, end="")
            f.close()
    elif k==2:
        print("Enter ::")
        print("\t  1.Exercise")
        print("\t  2.Food")
        c = int(input())
        if c==1:
            f=open("HarryExercise.txt")
            for i in f:
                print(i, end="")
            f.close()
        elif c==2:
            f=open("HarryFood.txt")
            for i in f:
                print(i, end="")
            f.close()
    elif k==3:
        print("Enter ::")
        print("\t  1.Exercise")
        print("\t  2.Food")
        c = int(input())
        if c==1:
            f = open("HammadExercise.txt")
            for i in f:
                print(i, end="")
            f.close()
        elif c==2:
            f = open("HammadFood.txt")
            for i in f:
                print(i, end="")
            f.close()
    else:
        print("Please enter valid input::")
        print("1.Rohan")
        print("Harry")
        print("Hammad")



print("HEALTH MANAGEMENT SYSTEM")
print("Enter number that you want")
print("1. Lock the value\n")
print("2. Retrieve the value\n")
var1 = int(input())

if var1==1:
    print("Enter ::")
    print("\t  1.Rohan")
    print("\t  2.Harry")
    print("\t  3.Hammad")
    var2 = int(input())
    take(var2)

else:
    print("Enter ::")
    print("\t  1.Rohan")
    print("\t  2.Harry")
    print("\t  3.Hammad")
    var2 = int(input())
    retrieve(var2)